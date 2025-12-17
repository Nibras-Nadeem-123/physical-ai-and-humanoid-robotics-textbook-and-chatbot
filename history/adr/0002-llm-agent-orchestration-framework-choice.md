# ADR-0002: LLM/Agent Orchestration Framework Choice

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-15
- **Feature:** 003-rag-chatbot-fastapi
- **Context:** The Physical AI Textbook RAG Chatbot requires a framework to integrate Large Language Models (LLMs) and orchestrate various agent behaviors, including reasoning over retrieved documents and managing agent skills. The project needs to support advanced agent capabilities as per the feature specification.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Use OpenAI Agents / ChatKit SDK for LLM integration and agent orchestration.

## Consequences

### Positive

- Streamlined development of agent behaviors, leveraging existing SDKs.
- Access to advanced agent capabilities and features.
- Faster iteration on agent logic.

### Negative

- Vendor lock-in to OpenAI's ecosystem.
- Potential cost implications for using OpenAI's services.
- Reliance on external API stability and terms of service.

## Alternatives Considered

- **Raw LLM completions with custom orchestration**: Offers maximum flexibility and cost control but requires significant development effort for agent logic and orchestration from scratch.
- **LangChain/LlamaIndex**: Popular open-source frameworks offering LLM orchestration. These are viable alternatives but might have a steeper learning curve or different architectural paradigms compared to OpenAI's native SDK, and could introduce additional dependencies.

## References

- Feature Spec: specs/003-rag-chatbot-fastapi/spec.md
- Implementation Plan: specs/003-rag-chatbot-fastapi/plan.md
- Related ADRs: N/A
- Evaluator Evidence: N/A