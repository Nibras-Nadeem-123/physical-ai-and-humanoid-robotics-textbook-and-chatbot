---
id: 0007
title: Revert to OpenAI API Key
stage: refactor
date: 2025-12-09
surface: agent
model: gemini
feature: 001-rag-chatbot-fastapi
branch: 001-rag-chatbot-fastapi
user: nibras_nadeem
command: N/A
labels: [refactor, openai]
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

use open ai api key instead of gemini api key

## Response snapshot

I have reverted the necessary files to use the OpenAI API key instead of the Gemini API key for the RAG chatbot feature.

Specifically:
- `backend/app/services/rag_pipeline.py` was reverted to initialize `client_openai` and use `gpt-3.5-turbo` for LLM calls, removing all OpenRouter/Gemini specific configurations.
- `backend/scripts/ingest.py` and `backend/tests/test_qdrant_retrieval.py` were reverted to use `client_openai` for embedding generation.
- `backend/README.md` and `.env.example` were updated to remove `GEMINI_API_KEY` and `GEMINI_BASE_URL` environment variables, and the `OPENAI_API_KEY` description was reverted to general usage.

The system now exclusively uses OpenAI API keys for both LLM answer generation and embedding generation.

## Outcome

- ✅ Impact: The RAG chatbot configuration has been reverted to use OpenAI API keys exclusively, fulfilling the user's request.
- 🧪 Tests: Existing tests (`backend/tests/test_qdrant_retrieval.py`) will now use the OpenAI client directly. Further testing is required to validate the OpenAI integration.
- 📁 Files: `backend/app/services/rag_pipeline.py`, `backend/scripts/ingest.py`, `backend/README.md`, `.env.example`, `backend/tests/test_qdrant_retrieval.py` were modified.
- 🔁 Next prompts: The configuration change is complete. I am awaiting the user's next instruction.
- 🧠 Reflection: The reversion process was straightforward, as it involved undoing previous changes.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): N/A