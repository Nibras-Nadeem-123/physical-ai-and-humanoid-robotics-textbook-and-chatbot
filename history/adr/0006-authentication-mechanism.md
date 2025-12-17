# ADR-0006: Authentication Mechanism

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 003-rag-chatbot-fastapi
- **Context:** The Physical AI Textbook RAG Chatbot requires a secure and reliable authentication and authorization mechanism for its users. The initial feature description specified "Support authentication using Better Auth," and further clarification during the `/sp.clarify` phase led to the decision to use JWT Token validation.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Implement user authentication and authorization via the "Better Auth" service using JWT Token validation (FastAPI issues/validates tokens).

## Consequences

### Positive

-   **Offloads Authentication Logic**: Leverages an external "Better Auth" service, simplifying the backend implementation by not reinventing user management, password hashing, etc.
-   **Scalability with JWTs**: JWTs are stateless, improving the scalability of the API service as no session state needs to be maintained on the server-side for each request.
-   **Standardized Security**: Utilizes a widely understood and adopted security mechanism (JWT) for authentication and authorization.
-   **Clear Separation of Concerns**: Aligns with Constitution Principle 7.

### Negative

-   **Dependency on External Service**: Relies on the availability and stability of the "Better Auth" service for core user authentication.
-   **JWT Security Challenges**: Requires careful handling of JWT security concerns, including proper storage (e.g., HTTP-only cookies), expiration management, and revocation strategies (e.g., blacklisting).
-   **Complexity for Frontend**: Frontend (embedded widget) needs to securely handle JWT tokens for API communication.

## Alternatives Considered

-   **API Key-based authentication**:
    -   **Pros**: Simple to implement.
    -   **Cons**: Generally less secure than token-based authentication for user sessions, harder to manage granular permissions, and not typically used for direct user authentication.
-   **OAuth 2.0 Authorization Code Flow**:
    -   **Pros**: A robust and highly secure flow, particularly well-suited for third-party client applications and more complex authorization scenarios.
    -   **Cons**: More complex to implement for a first-party application where direct JWT validation offers sufficient security and simpler integration, especially when leveraging an existing "Better Auth" service.
-   **Session-based authentication (with server-side sessions)**:
    -   **Pros**: Traditional method, potentially simpler state management on the server for some applications.
    -   **Cons**: Less scalable for distributed API services (requires sticky sessions or a shared session store), and harder to integrate seamlessly with embedded frontend widgets without cross-origin issues.

## References

- Feature Spec: specs/003-rag-chatbot-fastapi/spec.md (FR-001, Clarifications)
- Implementation Plan: specs/003-rag-chatbot-fastapi/plan.md (Auth Service (Better Auth), FastAPI Backend - JWT handling)
- API Contracts: specs/003-rag-chatbot-fastapi/contracts/openapi.yaml (JWTBearer security scheme)
- Initial feature description: "Support authentication using Better Auth"
- Constitution: .specify/memory/constitution.md (Principle 7: Clear Separation of Concerns (Auth, RAG, Agents))
- Related ADRs: N/A
- Evaluator Evidence: N/A