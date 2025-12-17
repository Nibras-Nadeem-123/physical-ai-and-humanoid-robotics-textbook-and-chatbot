---
id: 0006
title: Integrate Gemini via OpenRouter
stage: refactor
date: 2025-12-09
surface: agent
model: gemini
feature: 001-rag-chatbot-fastapi
branch: 001-rag-chatbot-fastapi
user: nibras_nadeem
command: N/A
labels: [refactor, gemini, openrouter]
links:
  spec: ./specs/001-rag-chatbot-fastapi/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - backend/app/services/rag_pipeline.py
  - backend/scripts/ingest.py
  - backend/README.md
  - .env.example
  - backend/tests/test_qdrant_retrieval.py
tests:
  - backend/tests/test_qdrant_retrieval.py
---

## Prompt

i don't have openai api key and don't want to buy it i want to work with gemini api key
C

## Response snapshot

The user confirmed that using the `openai` Python library configured for OpenRouter to access Gemini for LLM answers fulfills their intent. They also chose to proceed with the current setup for embeddings (requiring an `OPENAI_API_KEY`) due to technical blockers (network issues during `sentence-transformers` installation).

This means the integration of Gemini via OpenRouter is complete and the user accepts the current state regarding embeddings.

## Outcome

- ✅ Impact: The RAG chatbot now leverages Gemini models for answer generation via an OpenAI-compatible interface (OpenRouter), fulfilling the user's request to use Gemini. The user also explicitly accepted the current state of embeddings (requiring OpenAI API key) due to technical blockers.
- 🧪 Tests: Existing tests (`backend/tests/test_qdrant_retrieval.py`) were updated to reflect the change in client initialization. Further testing is required to validate the Gemini integration.
- 📁 Files: `backend/app/services/rag_pipeline.py`, `backend/scripts/ingest.py`, `backend/README.md`, `.env.example`, `backend/tests/test_qdrant_retrieval.py` were modified.
- 🔁 Next prompts: The integration is complete. No further action is required from me on this specific request.
- 🧠 Reflection: The user's intent was clear, and the change was implemented. The persistent network issue for embedding libraries remains a blocker for completely eliminating the `OPENAI_API_KEY` dependency, but the user has acknowledged and accepted this limitation for now.

## Evaluation notes (flywheel)

- Failure modes observed: Persistent network timeouts during `pip3 install sentence-transformers` (specifically `torch` dependency).
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): Address the embedding provider change to completely remove OpenAI API key dependency if network issues are resolved or a simpler alternative is found.
