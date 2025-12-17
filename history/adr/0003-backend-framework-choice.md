# ADR-0003: Backend Framework Choice

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 003-rag-chatbot-fastapi
- **Context:** The Physical AI Textbook RAG Chatbot requires a robust and performant backend to handle API requests from the frontend, orchestrate RAG processes, manage agent interactions, and integrate with various services (Auth, Qdrant, OpenAI).

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Use FastAPI as the primary backend framework.

## Consequences

### Positive

- High performance due to its ASGI nature.
- Strong type hinting for better code quality and maintainability.
- Excellent tooling for API development and documentation (automatic OpenAPI/Swagger UI generation).
- Good synergy with Python-based AI/ML libraries central to this project.

### Negative

- Python's Global Interpreter Lock (GIL) can limit true parallelism for CPU-bound tasks (though typically not a major issue for I/O-bound API services).
- Requires some familiarity with ASGI concepts for advanced use cases.

## Alternatives Considered

- **Node.js with Express/NestJS**: Offers a large ecosystem and good performance for I/O-bound tasks. While a strong general-purpose backend choice, Python's AI/ML ecosystem provides a more natural and efficient fit for the RAG and agent orchestration aspects of this project.
- **Flask**: A lighter-weight Python web framework. However, it requires more boilerplate for features like data validation, routing, and OpenAPI generation compared to FastAPI.
- **Django**: A full-stack Python web framework. It would be an overkill for a dedicated API backend unless extensive ORM, admin features, and templating are needed, which is not the primary focus here.

## References

- Feature Spec: specs/003-rag-chatbot-fastapi/spec.md
- Implementation Plan: specs/003-rag-chatbot-fastapi/plan.md
- Related ADRs: N/A
- Evaluator Evidence: N/A