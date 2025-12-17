# Deployment Guide for Physical AI Textbook RAG Chatbot

This guide outlines the steps to deploy the Physical AI Textbook RAG Chatbot to a containerized environment using Docker and Docker Compose.

## Prerequisites

-   Docker and Docker Compose installed on your deployment server.
-   Access to a PostgreSQL database (if not using the one in `docker-compose.yml`).
-   API keys for OpenAI, Qdrant, and Better Auth.

## 1. Environment Configuration

Create a `.env` file in the root of your project with the following variables:

```
# OpenAI API Key for embeddings and generative model
OPENAI_API_KEY="your_openai_api_key_here"

# Qdrant Vector Database
QDRANT_HOST="qdrant:6333" # Use "localhost:6333" if running outside docker-compose
QDRANT_API_KEY="your_qdrant_api_key_here"

# Better Auth Service
BETTER_AUTH_API_KEY="your_better_auth_api_key_here"
SECRET_KEY="a_strong_secret_key_for_jwt_signing" # **CHANGE THIS IN PRODUCTION**

# PostgreSQL Database
DATABASE_URL="postgresql://user:password@host:port/database_name" # e.g., postgresql://postgres:postgres@postgres:5432/rag_chatbot
POSTGRES_DB="rag_chatbot"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="postgres"

# Frontend API Base URL
REACT_APP_API_BASE_URL="http://localhost:8000/api/v1" # Change to your deployed backend URL
```
**Important**: Replace placeholder values with your actual production keys and URLs. Ensure `SECRET_KEY` is a strong, randomly generated string for production.

## 2. Initialize Database and Ingest Data

First, bring up the database and Qdrant services.

```bash
docker compose up -d postgres qdrant
```

Then, run database migrations (if you are using a migration tool like Alembic, otherwise ensure tables are created manually as per `docs/embedding_chatbot.md`).

Once your database is set up, ingest the textbook data into Qdrant:

```bash
# Ensure your data is in a directory, e.g., ./data/textbook_content
docker compose run --rm backend python backend/scripts/ingest.py --input-dir /app/data/textbook_content
```
Adjust `/app/data/textbook_content` to the path where your Markdown files are mounted inside the backend container.

## 3. Build and Deploy Services

Build and start all services using Docker Compose:

```bash
docker compose up --build -d
```

This will:
-   Build the FastAPI backend Docker image.
-   Build the Docusaurus frontend Docker image.
-   Start the backend, Qdrant, PostgreSQL, and frontend services.

## 4. Access the Application

-   **Frontend (Docusaurus)**: Accessible at `http://localhost:3000` (or the port you configured).
-   **FastAPI Backend (API)**: Accessible at `http://localhost:8000/api/v1` (or the port you configured).

## 5. Scaling and Production Considerations

-   **Reverse Proxy**: In a production environment, place a reverse proxy (e.g., Nginx, Caddy) in front of your frontend and backend services for SSL termination, load balancing, and static file serving.
-   **Database Management**: Use managed PostgreSQL services for better reliability, backups, and scaling.
-   **Qdrant Management**: For high availability, consider a Qdrant cluster or managed service.
-   **Secret Management**: Avoid storing secrets directly in `.env` files in production. Use a dedicated secret management solution (e.g., Docker Secrets, Kubernetes Secrets, HashiCorp Vault).
-   **Monitoring and Logging**: Integrate with monitoring and logging solutions (e.g., Prometheus, Grafana, ELK stack) for production visibility.

This guide provides a basic deployment overview. Specific production environments may require additional configurations and security measures.
