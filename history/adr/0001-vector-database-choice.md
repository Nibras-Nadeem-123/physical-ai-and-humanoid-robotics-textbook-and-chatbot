# ADR-0001: Vector Database Choice

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 003-rag-chatbot-fastapi
- **Context:** The Physical AI Textbook RAG Chatbot requires a vector database to store embeddings of the textbook content and perform similarity searches to retrieve relevant information for user queries. The project operates under a constraint of minimal latency on free-tier infrastructure.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Use Qdrant Cloud Free Tier as the primary vector database.

## Consequences

### Positive

- Aligns with free-tier infrastructure constraint, reducing operational overhead for self-hosting a vector database.
- Provides necessary vector search performance for RAG.

### Negative

- Dependency on an external cloud provider.
- Potential limitations of free tier (e.g., storage limits, rate limits) might become a bottleneck if usage scales significantly.

## Alternatives Considered

- **Self-hosted Qdrant**: Offers more control and scalability but introduces increased operational overhead and cost for hosting.
- **Pinecone (or similar managed vector databases)**: Provides managed service but may not have a free tier or might be more expensive than Qdrant's free tier.
- **Faiss (or other in-memory libraries)**: Suitable for smaller datasets or local development, but not scalable for a production system.

## References

- Feature Spec: specs/003-rag-chatbot-fastapi/spec.md
- Implementation Plan: specs/003-rag-chatbot-fastapi/plan.md
- Related ADRs: N/A
- Evaluator Evidence: N/A