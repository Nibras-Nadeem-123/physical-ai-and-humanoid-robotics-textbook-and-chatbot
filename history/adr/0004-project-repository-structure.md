# ADR-0004: Project Repository Structure

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 003-rag-chatbot-fastapi
- **Context:** The Physical AI Textbook RAG Chatbot is a new, standalone project intended to be integrated with an existing Docusaurus-based textbook. A decision is needed regarding its repository structure relative to the textbook to ensure efficient development, deployment, and maintenance.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Develop the chatbot in a separate Git repository, independent of the main textbook repository.

## Consequences

### Positive

-   **Clear Separation of Concerns**: Promotes modularity and reduces cognitive load by keeping the chatbot's codebase distinct.
-   **Independent Lifecycle Management**: Allows for independent versioning, deployment, and scaling of the chatbot without affecting the textbook.
-   **Focused Development**: Teams can work on the chatbot without needing deep knowledge or access to the entire textbook repository.
-   **Reduced Build/CI Times**: Build and test processes for the chatbot are isolated and typically faster.

### Negative

-   **Cross-Repository Dependencies**: Requires careful management of how the chatbot (e.g., its embedded widget) integrates with the Docusaurus textbook, potentially leading to versioning misalignment if not managed properly.
-   **Increased Overhead for Shared Resources**: Any shared configurations, build tools, or documentation between the chatbot and textbook might require duplication or more complex synchronization mechanisms.
-   **Potential for Integration Challenges**: Ensuring seamless integration (e.g., matching UI styles, passing data between IFrames/widgets) can require explicit design and effort.

## Alternatives Considered

-   **Monorepo Approach (chatbot within textbook repo)**:
    -   **Pros**: Could simplify integration (e.g., shared CI/CD, common dependencies, easier local development setup).
    -   **Cons**: Couples the chatbot's lifecycle to the textbook's, potentially increasing build/test times and complexity for both projects. Changes in one could inadvertently affect the other.
-   **Git Submodule/Subtree**:
    -   **Pros**: Offers some level of separation while keeping the code within a larger repository.
    -   **Cons**: Can add complexity to Git operations (e.g., cloning, updating submodules) and dependency management compared to a fully separate repository, often leading to developer friction.

## References

- Feature Spec: specs/003-rag-chatbot-fastapi/spec.md
- Implementation Plan: specs/003-rag-chatbot-fastapi/plan.md
- Initial feature description: "Be developed in a separate Git repository"
- Related ADRs: N/A
- Evaluator Evidence: N/A