# Detailed Task List for Physical AI Textbook RAG Chatbot Implementation

This document outlines the detailed tasks required to implement the "Physical AI Textbook RAG Chatbot" project, grouped by functional areas. Each task is designed to be atomic, testable, and clearly scoped.

## 1. Repository Setup

-   [X] **Task**: Initialize new Git repository for the chatbot project.
    -   **Description**: Create a new, empty Git repository for the chatbot project.
    -   **Test**: Verify repository is created and accessible.
-   [X] **Task**: Configure basic project structure (backend, frontend directories).
    -   **Description**: Set up `backend/`, `frontend/` directories and initial boilerplate files as per `plan.md`.
    -   **Test**: Verify directory structure and initial files are present.
-   [X] **Task**: Create initial `docker-compose.yml` for backend (FastAPI) and Qdrant.
    -   **Description**: Define Docker services for FastAPI application and Qdrant instance.
    -   **Test**: `docker compose up --build` runs without errors, Qdrant accessible.

## 2. Authentication (Better Auth)

-   [X] **Task**: Integrate Better Auth client library/SDK into FastAPI backend.
    -   **Description**: Add necessary dependencies and configuration for connecting to the Better Auth service.
    -   **Test**: Initialized client can connect to Better Auth.
-   [X] **Task**: Implement JWT token issuance/validation in FastAPI backend.
    -   **Description**: Create middleware or dependency to validate incoming JWTs from Better Auth and issue new JWTs upon successful login.
    -   **Test**: Unit tests for JWT validation logic, integration test for a protected endpoint.
-   [X] **Task**: Secure API endpoints with JWT authentication.
    -   **Description**: Apply FastAPI security dependencies to relevant endpoints (e.g., `/chat`).
    -   **Test**: Accessing protected endpoints without a valid JWT returns 401 Unauthorized.
-   [X] **Task**: Implement user login endpoint (`/auth/login`) in FastAPI.
    -   **Description**: Endpoint to receive user credentials, authenticate with Better Auth, and return a JWT.
    -   **Test**: Successful login returns a valid JWT; invalid credentials return 400.

### 2.5 User Consent Management

-   [X] **Task**: Implement explicit user consent prompt for data usage.
    -   **Description**: Develop UI/UX flows to obtain clear and explicit consent from users regarding data collection, storage, and usage (e.g., chat history, personal data).
    -   **Test**: User is presented with a clear consent prompt and can accept/decline.
-   [X] **Task**: Implement mechanism to record and manage user consent status.
    -   **Description**: Store user's consent decisions in the database, linked to their user profile.
    -   **Test**: Consent status is accurately recorded and retrieved.
-   [X] **Task**: Ensure data processing adheres to user consent status.
    -   **Description**: Implement checks in backend services to ensure personal data or conversation history is only processed in accordance with the user's recorded consent.
    -   **Test**: Data is not used if consent is not granted or revoked.

## 3. Text Ingestion & Chunking

-   [X] **Task**: Develop Markdown content parsing module.
    -   **Description**: Create Python module to parse `.md` and `.mdx` files, extracting raw text content.
    -   **Test**: Unit tests for parsing various Markdown syntax elements.
-   [X] **Task**: Implement semantic chunking logic for extracted text.
    -   **Description**: Develop a component that breaks down raw text into semantically meaningful chunks (FR-013).
    -   **Test**: Unit tests to verify chunking behavior produces coherent and appropriately sized segments.
-   [X] **Task**: Create data ingestion script (`backend/scripts/ingest.py`).
    -   **Description**: Script to orchestrate parsing, chunking, and preparing data for embedding.
    -   **Test**: Script runs successfully and outputs structured data.

## 4. Embeddings & Qdrant Indexing

-   [X] **Task**: Integrate OpenAI Embeddings API (or chosen alternative).
    -   **Description**: Add client library and configuration for `text-embedding-ada-002` (or alternative).
    -   **Test**: Unit tests for successful embedding generation from text.
-   [X] **Task**: Implement Qdrant client and connection.
    -   **Description**: Set up Python client for Qdrant, including connection details and API key.
    -   **Test**: Client can connect to Qdrant instance.
-   [X] **Task**: Design Qdrant collection schema for text chunks.
    -   **Description**: Define payload structure (text, source_ref, document_id) and vector parameters in Qdrant.
    -   **Test**: Qdrant collection created with correct schema.
-   [X] **Task**: Implement batch indexing of embeddings into Qdrant.
    -   **Description**: Extend ingestion script to generate embeddings for chunks and insert them into Qdrant.
    -   **Test**: Verify chunks and embeddings are successfully stored and retrievable from Qdrant.

## 5. RAG Query Pipeline

-   [ ] **Task**: Implement query embedding generation for user questions.
    -   **Description**: Use the same embedding model as for content to convert user queries into vectors.
    -   **Test**: Unit tests for query embedding.
-   [ ] **Task**: Implement vector similarity search in Qdrant for query retrieval.
    -   **Description**: Develop logic to query Qdrant with an embedded user question and retrieve top-k relevant text chunks.
    -   **Test**: Integration tests to verify relevant chunks are returned for example queries.
-   [X] **Task**: Integrate Generative Model (OpenAI Agents / ChatKit SDK) for response generation.
    -   **Description**: Set up client for the chosen generative model to synthesize answers from retrieved context.
    -   **Test**: Unit tests for basic text generation.
-   [X] **Task**: Construct RAG chain: Query -> Embed -> Retrieve -> Generate.
    -   **Description**: Combine the above components into a cohesive RAG pipeline in the FastAPI service.
    -   **Test**: End-to-end integration tests for the RAG pipeline.

## 6. Agent Orchestration

-   [ ] **Task**: Implement Agent Orchestration Layer core logic.
    -   **Description**: Develop the central component responsible for coordinating agent skills and subagents (FR-010).
    -   **Test**: Unit tests for basic routing decisions.
-   [X] **Task**: Design and implement Agent Skill registry mechanism.
    -   **Description**: Create a database table (PostgreSQL) or configuration to store metadata about available Agent Skills.
    -   **Test**: Skills can be registered and retrieved from the registry.
-   [X] **Task**: Implement dynamic loading mechanism for Agent Skills (Python classes).
    -   **Description**: Develop logic to load Python classes based on registry metadata (FR-009).
    -   **Test**: Unit tests for dynamic loading and instantiation of skill classes.

## 7. Subagents & Skill System

-   [X] **Task**: Define common interface for Agent Skills (Python class structure).
    -   **Description**: Establish the abstract base class or interface that all Agent Skills must adhere to (FR-008).
    -   **Test**: Sample skill classes can implement the interface without errors.
-   [X] **Task**: Develop initial "ROS2 Tutor" Agent Skill.
    -   **Description**: Implement a sample Agent Skill focusing on ROS2 topics.
    -   **Test**: Unit tests for the "ROS2 Tutor" skill's functionality.
-   [X] **Task**: Develop initial "Humanoid Control Expert" Agent Skill.
    -   **Description**: Implement a sample Agent Skill focusing on humanoid control.
    -   **Test**: Unit tests for the "Humanoid Control Expert" skill's functionality.

## 8. Citation & Reference System

-   [X] **Task**: Implement extraction of source references from retrieved chunks.
    -   **Description**: Ensure that when chunks are retrieved, their `source_ref` is available for citation.
    -   **Test**: Verify `source_ref` is correctly propagated through the RAG pipeline.
-   [X] **Task**: Format generated answers with plain text references (e.g., 'Chapter 1, Section 2.3, Paragraph 4').
    -   **Description**: Develop a post-processing step for generative model output to insert plain text citations.
    -   **Test**: Unit tests for correct plain text citation formatting.
-   [X] **Task**: Generate direct hyperlinks to Docusaurus sections for references.
    -   **Description**: Map `source_ref` to Docusaurus URL structure to create clickable links (FR-012).
    -   **Test**: Unit tests for correct hyperlink generation.

## 9. Frontend Embed Widget

-   [X] **Task**: Develop core JavaScript widget for chatbot UI.
    -   **Description**: Create an independent frontend component for chat input/output and selected text handling.
    -   **Test**: Widget renders correctly in a standalone HTML page.
-   [X] **Task**: Implement API client in frontend widget for FastAPI backend.
    -   **Description**: Use `fetch` or a library (e.g., `axios`) to communicate with the FastAPI `/chat` and `/auth/login` endpoints.
    -   **Test**: Widget can successfully send requests and receive responses.
-   [ ] **Task**: Integrate JWT handling in frontend for authenticated API calls.
    -   **Description**: Store and attach JWT to outgoing requests.
    -   **Test**: Authenticated calls succeed; unauthenticated calls fail.
-   [X] **Task**: Implement selected text capture and transmission to backend.
    -   **Description**: Add functionality to capture user's text selection and include it in chat queries.
    -   **Test**: Selected text is accurately sent to the backend.

## 10. Integration with Textbook (Docusaurus)

-   [X] **Task**: Implement embedding mechanism (iframe or JS widget) for Docusaurus.
    -   **Description**: Provide clear instructions and code snippets for Docusaurus administrators to embed the chatbot (FR-007).
    -   **Test**: Chatbot widget successfully embeds and functions within a Docusaurus page.
-   [X] **Task**: Ensure chatbot state persistence/management across Docusaurus page navigations.
    -   **Description**: Implement mechanisms (e.g., local storage, URL parameters) to maintain conversation context if the user navigates pages.
    -   **Test**: Conversation history is retained when navigating Docusaurus pages.

## 11. Security & Rate Limiting

-   [X] **Task**: Implement basic rate limiting for API endpoints.
    -   **Description**: Use FastAPI middleware or a library to limit requests per IP/user to prevent abuse.
    -   **Test**: Exceeding rate limit results in appropriate error responses.
-   [X] **Task**: Implement input validation and sanitization for all user inputs.
    -   **Description**: Prevent common vulnerabilities (e.g., XSS, injection) in user queries and other inputs.
    -   **Test**: Unit tests for validation rules.
-   [X] **Task**: Configure CORS headers for FastAPI backend.
    -   **Description**: Allow frontend (Docusaurus) to securely access the backend API.
    -   **Test**: Frontend can make cross-origin requests without issues.

## 12. Deployment Readiness

-   [X] **Task**: Finalize Dockerfile for FastAPI backend.
    -   **Description**: Create an optimized Dockerfile for the FastAPI application.
    -   **Test**: Docker image builds successfully and runs locally.
-   [X] **Task**: Finalize Dockerfile for Frontend (Docusaurus build).
    -   **Description**: Create a Dockerfile to build and serve the Docusaurus frontend.
    -   **Test**: Docker image builds successfully and serves the static site.
-   [X] **Task**: Configure production `docker-compose.yml` for containerized deployment.
    -   **Description**: Set up production-ready Docker Compose configuration, including environment variables and volumes.
    -   **Test**: Local deployment mirrors production environment setup.
-   [X] **Task**: Document deployment instructions for containerized environment.
    -   **Description**: Provide clear steps for deploying the backend and frontend to a container orchestration platform (e.g., Kubernetes, simple Docker host) (FR-014).
    -   **Test**: Deployment steps are clear and actionable.