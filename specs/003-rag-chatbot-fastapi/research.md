# Research for Physical AI Textbook RAG Chatbot

This document captures research decisions made during Phase 0 planning.

## 1. Specific RDBMS for metadata and conversation history

**Decision**: PostgreSQL
**Rationale**: PostgreSQL is a robust, open-source relational database known for its reliability, extensive feature set (including JSONB support which can be useful for flexible metadata storage), and strong community support. It is a common choice for backend services built with FastAPI and provides good performance characteristics that can be optimized for free-tier infrastructure.
**Alternatives considered**: SQLite (too simple for potential scalability needs), MySQL (good alternative, but PostgreSQL's features are slightly preferred for flexibility).

## 2. Specific embedding model to be used

**Decision**: OpenAI's `text-embedding-ada-002` (or a suitable open-source alternative like `BAAI/bge-small-en` if cost/licensing becomes a critical factor).
**Rationale**: `text-embedding-ada-002` is a widely adopted, high-quality embedding model from OpenAI that is known for its performance and general applicability. For free-tier constraints, exploring a smaller, performant open-source model like `BAAI/bge-small-en` is a pragmatic alternative to manage costs while maintaining quality. The final decision will depend on a cost-benefit analysis and performance benchmarking during implementation.
**Alternatives considered**: Other OpenAI embedding models (more expensive), various open-source embedding models (require more local compute/management).