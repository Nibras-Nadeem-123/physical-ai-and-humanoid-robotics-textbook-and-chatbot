# Quickstart Guide: Physical AI Textbook RAG Chatbot

This guide provides a rapid setup and usage overview for the "Physical AI Textbook RAG Chatbot" system.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

-   Docker and Docker Compose (for containerized deployment)
-   Python 3.11
-   `pip` (Python package installer)
-   `git`

## 2. Setup

### 2.1 Clone the Repository

```bash
git clone [REPOSITORY_URL]
cd [REPOSITORY_NAME]
```

### 2.2 Configure Environment Variables

Create a `.env` file in the `backend/` directory based on `backend/.env.example`. You will need to provide:

-   `OPENAI_API_KEY`: Your API key for OpenAI (for ChatKit/Agents, embeddings).
-   `QDRANT_HOST`: Host for your Qdrant instance (e.g., from Qdrant Cloud Free Tier).
-   `QDRANT_API_KEY`: API key for your Qdrant instance.
-   `BETTER_AUTH_API_KEY`: API key for your Better Auth service.
-   `DATABASE_URL`: Connection string for your PostgreSQL database.

Example `backend/.env` contents:

```
OPENAI_API_KEY="sk-..."
QDRANT_HOST="your-qdrant-cloud-host"
QDRANT_API_KEY="your-qdrant-api-key"
BETTER_AUTH_API_KEY="your-better-auth-api-key"
DATABASE_URL="postgresql://user:password@host:port/database"
```

### 2.3 Ingest Textbook Content

Place your Markdown textbook files (`.md`, `.mdx`) in a designated input directory (e.g., `backend/data/textbook/`). Then, run the ingestion script:

```bash
# From the project root
python backend/scripts/ingest.py --input-dir backend/data/textbook/
```
This script will process the Markdown files, chunk them semantically, generate embeddings, and store them in your configured Qdrant instance.

### 2.4 Build and Run with Docker Compose

Navigate to the project root and start the services:

```bash
docker compose up --build
```
This will build and run the FastAPI backend and the Docusaurus frontend in separate containers.

## 3. Usage

### 3.1 Access the Frontend

Open your web browser and navigate to `http://localhost:3000` (or the port where Docusaurus is running). You should see the textbook website with the embedded chatbot widget.

### 3.2 Interact with the Chatbot

1.  **Login**: Use the frontend's login functionality, which will interact with the Better Auth service via the FastAPI backend.
2.  **Ask Questions**:
    *   Type a question in the chatbot's input field and press Enter for full-book queries.
    *   Select text in the textbook, then type a question in the chatbot's input field to ask about the selected context.
3.  **Review Answers**: The chatbot will provide answers with citations (plain text and hyperlinks) from the textbook.

## 4. Advanced: Developing Agent Skills

Agent skills are Python classes adhering to a defined interface. To add a new skill:

1.  Create a new Python file in `backend/src/agents/`.
2.  Define a class that implements the required skill interface (e.g., `execute(query: str, context: dict) -> str`).
3.  Register the skill's metadata (name, description) in your database or configuration as per the Agent Orchestration Layer's requirements.
4.  The Agent Orchestration Layer will dynamically discover and load your new skill.