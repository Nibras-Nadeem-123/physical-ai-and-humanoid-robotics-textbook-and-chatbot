---
id: 0001
title: Create RAG Chatbot Constitution
stage: constitution
date: 2025-12-15
surface: agent
model: gemini-1.5-pro-a001
feature: none
branch: 003-rag-chatbot-fastapi
user: N/A
command: /sp.constitution Create a project constitution for the “Physical AI Textbook RAG Chatbot”. Principles to include: - Accuracy over creativity - Retrieval-first, generation-second - No hallucinations without citations - Explicit user consent for data usage - Minimal latency on free-tier infrastructure - Modular, reusable intelligence (Agent Skills) - Clear separation of concerns (auth, RAG, agents) Ensure: - The constitution aligns with the feature spec - All future plans and tasks must comply with these principles
labels: []
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:
- 
---

## Prompt

Create a project constitution for the “Physical AI Textbook RAG Chatbot”. Principles to include: - Accuracy over creativity - Retrieval-first, generation-second - No hallucinations without citations - Explicit user consent for data usage - Minimal latency on free-tier infrastructure - Modular, reusable intelligence (Agent Skills) - Clear separation of concerns (auth, RAG, agents) Ensure: - The constitution aligns with the feature spec - All future plans and tasks must comply with these principles

## Response snapshot

The agent created the initial project constitution for the 'Physical AI Textbook RAG Chatbot' at `.specify/memory/constitution.md`, incorporating the specified principles and governance. The constitution is version 1.0.0. Several template files were flagged for manual review to ensure alignment.

## Outcome

- ✅ Impact: The project constitution has been established.
- 🧪 Tests: N/A
- 📁 Files: `.specify/memory/constitution.md` created/modified.
- 🔁 Next prompts: Continue with project development based on the established constitution.
- 🧠 Reflection: Successfully created a new constitution based on user input, including handling a non-template starting point.

## Evaluation notes (flywheel)

- Failure modes observed: Incorrect `stage` used for `create-phr.sh` initially.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A