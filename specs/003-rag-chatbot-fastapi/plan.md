# Implementation Plan: Physical AI Textbook RAG Chatbot

**Branch**: `003-rag-chatbot-fastapi` | **Date**: 2025-12-15 | **Spec**: [specs/003-rag-chatbot-fastapi/spec.md](specs/003-rag-chatbot-fastapi/spec.md)
**Input**: Feature specification from `/specs/003-rag-chatbot-fastapi/spec.md`

## Summary

The "Physical AI Textbook RAG Chatbot" project aims to provide an intelligent Q&A system for a Physical AI & Humanoid Robotics textbook. It will use a FastAPI backend, OpenAI Agents/ChatKit SDK for reasoning, and Qdrant for vector storage. Users can ask questions about the entire book or selected text, receiving answers with citations. The chatbot will be embeddable in the Docusaurus-based textbook website, supporting modular Agent Skills and Subagents. The system prioritizes accuracy, retrieval-first responses, and minimal latency on cost-effective infrastructure, with a clear separation of concerns.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, OpenAI Agents / ChatKit SDK, Qdrant, Better Auth SDK/client
**Storage**: Qdrant (vector database) for embeddings and RAG, PostgreSQL for user data, conversation history, and skill metadata.
**Testing**: pytest
**Target Platform**: Linux servers (for FastAPI backend), Web browsers (for Docusaurus frontend and embedded widget)
**Project Type**: Web application (frontend + backend)
**Performance Goals**:
- Average time from question submission to receiving a full answer MUST be < 5 seconds (SC-002).
- System MUST handle 50 concurrent users without significant degradation (>10s response time) (SC-004).
**Constraints**:
- Minimal latency on free-tier infrastructure (Constitution, Principle 5).
- Embeddable (iframe or JS widget) into Docusaurus website (FR-007).
**Scale/Scope**: Physical AI Textbook RAG Chatbot, supporting full-book and selected-text queries. Initially targeting a single textbook.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The following principles from the Project Constitution (Version 1.0.0, dated 2025-12-15) are directly applicable to this implementation plan and must be adhered to:

-   **Principle 1: Accuracy Over Creativity**: The RAG pipeline and agent responses MUST prioritize factual accuracy from the textbook.
-   **Principle 2: Retrieval-First, Generation-Second**: The RAG architecture MUST ensure content retrieval precedes generation.
-   **Principle 3: No Hallucinations Without Citations**: Generative outputs MUST be traceable and cited from the textbook.
-   **Principle 4: Explicit User Consent for Data Usage**: All data handling MUST adhere to explicit user consent.
-   **Principle 5: Minimal Latency on Free-Tier Infrastructure**: Design decisions MUST consider and optimize for minimal latency within budget constraints.
-   **Principle 6: Modular, Reusable Intelligence (Agent Skills)**: Agent and subagent design MUST be modular and promote skill reusability.
-   **Principle 7: Clear Separation of Concerns (Auth, RAG, Agents)**: Architectural design MUST ensure distinct boundaries between authentication, RAG, and agent components.

## Project Structure

### Documentation (this feature)

```text
specs/003-rag-chatbot-fastapi/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── app/
│   │   ├── main.py        # FastAPI app entrypoint
│   │   ├── api/           # API endpoints (auth, chat)
│   │   ├── core/          # Configuration, security (JWT handling)
│   │   ├── models/        # Pydantic models for requests/responses, data
│   │   └── services/      # Business logic (chat, RAG, agent orchestration)
│   ├── agents/            # Agent skill definitions (Python classes adhering to interface)
│   └── data_ingestion/    # Scripts/modules for content ingestion
└── tests/

frontend/
├── src/
│   ├── components/Chatbot/ # Chatbot UI component (embeddable)
│   ├── services/api.js    # Frontend API client
│   └── hooks/             # Frontend-specific hooks
└── package.json

# Structure Decision: The "Option 2: Web application" structure is selected due to the clear frontend and backend separation.
# It is customized to include specific directories for agent skills and data ingestion within the backend,
# and a dedicated Chatbot component within the frontend.
```

## High-Level Architecture (Text Description)

The system will operate as a web application with a clear separation between a FastAPI backend and a Docusaurus-integrated frontend.

1.  **Frontend (Docusaurus Integration)**:
    *   A JavaScript widget/iframe will be embedded into the Docusaurus textbook, serving as the user interface for the chatbot.
    *   This component will handle user input, display chatbot responses, and manage selected text context.
    *   It will communicate with the FastAPI backend via a RESTful API.

2.  **FastAPI Backend**:
    *   Serves as the central API gateway and orchestrator.
    *   Handles user authentication and authorization using JWT Token validation (FR-001).
    *   Routes user queries to the RAG Pipeline or Agent Orchestration Layer.
    *   Manages conversation state by persisting it in PostgreSQL. Conversation history will be retained for [NEEDS CLARIFICATION: How long should conversation history be retained? E.g., 30 days, indefinitely, configurable?].

3.  **Auth Service (Better Auth)**:
    *   An external or integrated service handling user registration, login, and potentially user profile management.
    *   Interacts with the FastAPI backend to issue/validate JWT tokens.

4.  **Embedding Pipeline**:
    *   Responsible for processing ingested textbook content (Markdown files) (FR-015).
    *   Uses semantic chunking to break down content into meaningful units (FR-013).
    *   Generates embeddings for these chunks using OpenAI's `text-embedding-ada-002` (or a suitable open-source alternative like `BAAI/bge-small-en`) as the embedding model.
    *   Stores chunks and their embeddings in Qdrant.

5.  **Qdrant Vector Store**:
    *   Serves as the vector database for storing textbook content embeddings.
    *   Efficiently retrieves relevant text chunks based on user query embeddings.

6.  **RAG Pipeline**:
    *   Takes user queries, generates embeddings.
    *   Performs vector similarity search in Qdrant to retrieve top-k relevant textbook chunks.
    *   Feeds retrieved chunks and user query to the Generative Model for response generation.

7.  **Agent Orchestration Layer**:
    *   Coordinates the execution of various "Agent Skills" and "Subagents".
    *   Decides which skills/subagents are relevant based on the user's query and context.
    *   Dynamically loads and registers Agent Skills (Python classes adhering to a defined interface) (FR-009).

8.  **Subagent & Skill Registry**:
    *   A mechanism (e.g., database, configuration files) to store metadata about available Agent Skills and Subagents.
    *   Facilitates dynamic discovery and loading by the Agent Orchestration Layer.
    *   Agent Skills are packaged as Python classes adhering to a defined interface (FR-008).

## Data Flow

### Full-Book Queries

1.  **User Input**: User submits a question through the embedded frontend widget.
2.  **Frontend to Backend**: Widget sends query to FastAPI backend with user's JWT.
3.  **Auth Check**: FastAPI validates JWT with Better Auth.
4.  **Query Embedding**: FastAPI's RAG component embeds the user query.
5.  **Retrieval (Qdrant)**: Embedded query is used to find top-k relevant chunks across the entire textbook in Qdrant.
6.  **Generation**: Retrieved chunks and original query are sent to the generative model (OpenAI Agents / ChatKit SDK) for answer synthesis.
7.  **Response & Citation**: Generative model returns an answer, which is processed to include plain text and hyperlink citations (FR-012).
8.  **Backend to Frontend**: FastAPI sends the structured answer back to the widget.
9.  **Display**: Widget displays the answer and citations to the user.

### Selected-Text-Only Queries

1.  **User Input**: User selects text in Docusaurus, then submits a question via the widget, indicating "selected text context."
2.  **Frontend to Backend**: Widget sends query, selected text, and user's JWT to FastAPI.
3.  **Auth Check**: FastAPI validates JWT.
4.  **Focused Retrieval**: FastAPI's RAG component uses the selected text as an additional contextual filter or primary retrieval target within Qdrant (e.g., filtering chunks to only those within the selected text's vicinity or embedding the selected text itself).
5.  **Generation**: Retrieved chunks (constrained by selected text) and original query are sent to the generative model for answer synthesis.
6.  **Response & Citation**: Generative model returns an answer, processed for citations.
7.  **Backend to Frontend**: FastAPI sends the structured answer back to the widget.
8.  **Display**: Widget displays the answer and citations.

## Skill Loading Workflow (Matrix-style intelligence)

The Agent Orchestration Layer will manage Agent Skills.

1.  **Skill Definition**: Agent Skills are defined as Python classes adhering to a common interface, specifying their capabilities and input/output requirements.
2.  **Registration**: Skills are registered with the Subagent & Skill Registry (e.g., a database table or a dedicated service) upon system startup or dynamically. This includes metadata like skill name, description, and conditions for activation.
3.  **Dynamic Loading**: When the Agent Orchestration Layer determines a specific skill is needed (based on user query, context, or internal state), it dynamically loads the corresponding Python class.
4.  **Execution**: The loaded skill class is instantiated and executed with the necessary inputs.
5.  **Unloading/Caching**: Skills can be unloaded or cached after use to manage resources, depending on system load and frequency of use.

## Error Handling & Fallback Strategies

-   **RAG Pipeline Failures**:
    *   If Qdrant retrieval fails: Fallback to a broader search or inform the user of retrieval issues.
    *   If generative model API fails: Inform the user, potentially suggest rephrasing or trying later.
-   **Authentication Failures**:
    *   Invalid JWT: Redirect to login, prompt for re-authentication.
    *   Unauthorized access: Inform the user of insufficient permissions.
-   **Agent Skill Execution Errors**:
    *   If a specific skill fails: Attempt to use an alternative skill, or use a general fallback response.
    *   Log errors with context for debugging.
-   **User Input Errors**:
    *   Malformed queries: Prompt user to rephrase.
    *   Off-topic questions: Use FR-011 strategy (state limitations, suggest rephrasing within textbook context).
-   **General System Errors**: Implement robust logging, monitoring, and alerts. Graceful degradation where possible.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |