# Feature Specification: Standalone RAG Chatbot

**Feature Branch**: `002-rag-chatbot-fastapi`
**Created**: 2025-12-15
**Status**: Draft
**Input**: User description: "Create a complete feature specification for a standalone Retrieval-Augmented Generation (RAG) chatbot system. Project name: Physical AI Textbook RAG Chatbot Purpose: Build a secure, production-ready chatbot that allows authenticated users to ask questions about the “Physical AI & Humanoid Robotics” textbook. Core requirements: - Chatbot answers questions using only textbook content - Supports two modes: 1) Full-book question answering 2) Question answering restricted to user-selected text - Every answer must include references (chapter + section) - No hallucinations outside the indexed content Architecture requirements: - Backend: FastAPI - Vector database: Qdrant Cloud (free tier) - LLM access via OpenAI Agents / ChatKit SDK - Document ingestion pipeline (markdown + PDF support) - Chunking, embedding, indexing strategy explicitly defined Security & access: - Authentication required before chat access - Support OAuth (Google/GitHub) or email magic-link - Rate limiting per user - No public anonymous access Frontend: - Web UI with chat interface - Ability to select text from the textbook and ask questions on that selection - Display cited sources inline Non-functional requirements: - Modular architecture - Environment-based config - Designed for future integration into an external Docusaurus textbook site - Clear API boundaries for embedding into another site Deliverables: - spec.md describing full system behavior - API contracts - Data flow diagrams (textual) - Explicit out-of-scope items"

## Clarifications

### Session 2025-12-15

- Q: How should the API differentiate between a general (full-book) question and a question on a selected text snippet? → A: Use two separate endpoints (e.g., `POST /chat` for general questions and `POST /chat-contextual` for questions on selected text).
- Q: What is the desired user experience when an authentication token expires mid-chat? → A: Display a modal or a banner that says "Your session has expired" with a "Log in again" button that re-initiates the authentication flow.
- Q: What is the desired strategy for updating the search index when the textbook content changes? → A: Automatic nightly job that checks for and indexes new/updated content.
- Q: What format should the chatbot use for citing sources from the textbook in its answers? → A: `chapter X, section Y, page no 0012, line no 4`

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Authenticated User Asks a Question on the Full Textbook (Priority: P1)

An authenticated user logs into the chatbot, asks a question in the chat interface, and receives an answer generated exclusively from the content of the "Physical AI & Humanoid Robotics" textbook. The answer includes citations to the relevant chapter and section.

**Why this priority**: This is the core functionality of the chatbot and provides the primary value to the user.

**Independent Test**: This can be tested by logging in as a user, asking a question, and verifying that the answer is relevant, accurate, and contains a valid citation.

**Acceptance Scenarios**:

1.  **Given** an authenticated user is on the chat page, **When** they enter a question about the textbook and submit, **Then** the system displays an answer with source citations.
2.  **Given** an authenticated user asks a question with no answer in the textbook, **When** they submit the question, **Then** the system responds that it cannot answer the question based on the available content.

---

### User Story 2 - Authenticated User Asks a Question on a Selected Text Snippet (Priority: P2)

A user on the textbook website selects a specific paragraph or section of text, right-clicks (or uses a similar mechanism) to trigger a context menu, and selects "Ask a question on this selection." A chat interface appears, and the user can ask a question that the chatbot will answer using only the selected text as context.

**Why this priority**: This provides a more focused and contextual way for users to interact with the content, enhancing the learning experience.

**Independent Test**: Can be tested by selecting text on a page, initiating the contextual chat, and verifying the answer is constrained to the selected text.

**Acceptance Scenarios**:

1.  **Given** a user has selected a block of text on the textbook page, **When** they invoke the contextual chat and ask a relevant question, **Then** the system provides an answer generated only from the selected text.
2.  **Given** a user has invoked the contextual chat on a selected text, **When** they ask a question outside the scope of that text, **Then** the system indicates it cannot answer from the provided context.

---

### User Story 3 - Automatic Content Ingestion and Indexing (Priority: P3)

The system automatically processes and indexes new or updated textbook content (in Markdown or PDF format) via a nightly job. This job chunks the documents, generates embeddings, and indexes them into the vector database, making the new content available for the chatbot to use.

**Why this priority**: This is critical for maintaining the knowledge base of the chatbot but is a background administrative task, not a direct user-facing feature.

**Independent Test**: Can be tested by running the ingestion script with new content and then verifying that the chatbot can answer questions based on that new content.

**Acceptance Scenarios**:

1.  **Given** a new PDF or Markdown file of a textbook chapter, **When** the administrator runs the ingestion script, **Then** the content is successfully indexed and becomes searchable.
2.  **Given** a malformed or unsupported file type, **When** the administrator runs the ingestion script, **Then** the system logs an error and does not add the content to the index.

---

### Edge Cases

-   What happens if a user's authentication token expires during a chat session? **Answer**: A modal or banner will be displayed to the user, prompting them to log in again. The user can then re-authenticate to continue their session.
-   How does the system handle extremely long questions or questions that are nonsensical?
-   What is the behavior when the vector database or the external LLM is unavailable?
-   How does the system handle multiple users asking questions simultaneously?

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The system MUST require user authentication before allowing access to the chat functionality.
- **FR-002**: The system MUST support GitHub OAuth for authentication.
-   **FR-003**: The chatbot MUST generate answers based solely on the indexed content of the "Physical AI & Humanoid Robotics" textbook.
-   **FR-004**: Every answer generated by the chatbot MUST include a reference to the source, formatted as: `chapter X, section Y, page no P, line no L`.
-   **FR-005**: The system MUST provide a mechanism to ingest and index new textbook content from Markdown and PDF files.
-   **FR-011**: The system MUST automatically update the search index nightly to incorporate new or updated textbook content.
-   **FR-006**: The system MUST support two modes of interaction: a general chat mode for the entire textbook and a contextual chat mode for user-selected text snippets.
-   **FR-007**: The system MUST implement rate limiting for authenticated users to prevent abuse, specifically 60 requests per minute and 600 requests per hour.
-   **FR-008**: The system's chat interface MUST be embeddable into an external Docusaurus website.
-   **FR-009**: The system MUST NOT provide any public or anonymous access to the chat functionality.
-   **FR-010**: When a question cannot be answered from the textbook content, the system MUST respond with: "I cannot answer this question. Please ensure your question is related to the content of the 'Physical AI & Humanoid Robotics' textbook."

### Key Entities

-   **User**: Represents an authenticated individual interacting with the chatbot. Key attributes: User ID, authentication provider, rate limit counter.
-   **Chat Session**: Represents a single conversation between a user and the chatbot. Key attributes: Session ID, User ID, conversation history.
-   **Document Chunk**: Represents a piece of text from the textbook that has been indexed. Key attributes: Chunk ID, content, source (chapter/section), embedding vector.

### API Contracts

Based on clarification, the system will use two separate endpoints.

- `POST /chat`
  - **Description**: Handles general questions against the full textbook.
  - **Authentication**: Required.
  - **Request Body**: `{"question": "string"}`
  - **Success Response (200 OK)**: `{"answer": "string", "references": [{"chapter": "string", "section": "string"}]}`

- `POST /chat-contextual`
  - **Description**: Handles questions against a user-selected text snippet.
  - **Authentication**: Required.
  - **Request Body**: `{"question": "string", "selected_text": "string"}`
  - **Success Response (200 OK)**: `{"answer": "string"}`

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: 95% of answers generated by the chatbot must be factually consistent with the indexed textbook content.
-   **SC-002**: 99% of chatbot answers for questions within the scope of the textbook must include a valid and accurate source citation.
-   **SC-003**: The median response time for a chatbot query, from question submission to the first token of the answer, must be less than 3 seconds.
-   **SC-004**: The system must be able to ingest a 500-page PDF textbook in under 30 minutes.
-   **SC-005**: The system must maintain an uptime of 99.9%.

## Out of Scope

-   Real-time conversation with multiple users in a single "room".
-   Saving or persisting user chat history across sessions.
-   A user interface for administrators to manage content ingestion.
-   Any chatbot capabilities beyond question-answering on the provided textbook.