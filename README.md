# Physical AI Textbook RAG Chatbot

## Project Title
Physical AI Textbook RAG Chatbot

## Description
The "Physical AI Textbook RAG Chatbot" is an intelligent Q&A system designed for a Physical AI & Humanoid Robotics textbook. It leverages a FastAPI backend, OpenAI Agents/ChatKit SDK for advanced reasoning, and Qdrant as a vector database for efficient information retrieval. Users can ask questions about the entire textbook or selected text snippets, receiving accurate answers augmented with citations from the source material. The chatbot is designed to be seamlessly embeddable within the Docusaurus-based textbook website, supporting modular Agent Skills and Subagents for specialized interactions. The system prioritizes factual accuracy, retrieval-first responses, minimal latency, and a clear separation of concerns in its architecture.

## Features
-   **FastAPI Backend**: Robust and scalable API for chatbot functionalities.
-   **Authentication**: Secure user authentication and authorization using JWT with Better Auth integration.
-   **User Consent Management**: Explicit user consent for data usage and privacy adherence.
-   **Qdrant Vector Database**: Efficient storage and retrieval of textbook content embeddings.
-   **OpenAI Embeddings API**: Generates high-quality vector embeddings for text chunks and user queries.
-   **RAG Query Pipeline**: Combines embedding, retrieval, and generative models for accurate, context-aware responses.
-   **Agent Orchestration Layer**: Coordinates various modular Agent Skills and Subagents for specialized interactions.
-   **Dynamic Skill Loading**: Agent Skills (Python classes) are dynamically loaded based on their registry metadata.
-   **ROS2 Tutor Agent Skill**: Provides information and tutorials on ROS2 topics.
-   **Humanoid Control Expert Agent Skill**: Offers expert advice and solutions for humanoid robot control systems.
-   **Citation-Aware Response Logic**: Generates answers with plain text citations and potential hyperlinks to Docusaurus sections.
-   **Frontend Chatbot Widget**: An independent, embeddable JavaScript widget for chat interaction.
-   **Docusaurus Integration**: Clear instructions and mechanisms for embedding the chatbot into a Docusaurus website.
-   **State Persistence**: Chatbot conversation history and session management using local storage.
-   **Security & Rate Limiting**: Basic rate limiting for API endpoints, input validation, and CORS configuration.
-   **Containerized Deployment**: Dockerized backend and frontend for easy deployment using Docker Compose.

## Architecture
The system is a web application with a FastAPI backend and a Docusaurus-integrated frontend.

1.  **Frontend (Docusaurus Integration)**:
    *   A JavaScript widget is embedded into the Docusaurus textbook for user interaction.
    *   Handles user input, displays responses, manages selected text, and communicates with the FastAPI backend via RESTful API.

2.  **FastAPI Backend**:
    *   Acts as the central API gateway and orchestrator.
    *   Manages user authentication (JWT token validation) and routes queries to either the RAG Pipeline or the Agent Orchestration Layer.

3.  **Auth Service (Better Auth)**:
    *   Handles user registration and login, issuing/validating JWT tokens with the FastAPI backend.

4.  **Embedding Pipeline**:
    *   Processes Markdown textbook content, performs semantic chunking, and generates embeddings using OpenAI's `text-embedding-ada-002`.
    *   Stores content chunks and their embeddings in Qdrant.

5.  **Qdrant Vector Store**:
    *   Stores textbook content embeddings, enabling efficient vector similarity search.

6.  **RAG Pipeline**:
    *   Embeds user queries, retrieves relevant chunks from Qdrant, and synthesizes answers using a generative model.
    *   Formats responses with citations.

7.  **Agent Orchestration Layer**:
    *   Coordinates Agent Skills and Subagents, dynamically loading and executing them based on query context.

8.  **Subagent & Skill Registry**:
    *   A PostgreSQL database stores metadata about available Agent Skills for dynamic discovery and loading.

## Setup

### Prerequisites
-   Docker and Docker Compose
-   Python 3.11
-   Node.js 20.x

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/physical-ai-and-humanoid-robotic-textbook.git
cd physical-ai-and-humanoid-robotic-textbook
```

### 2. Environment Configuration
Create a `.env` file in the project root based on `docs/deployment_guide.md` and populate it with your API keys and database credentials.

### 3. Database Initialization & Data Ingestion
Start PostgreSQL and Qdrant services:
```bash
docker compose up -d postgres qdrant
```
Run data ingestion to populate Qdrant with textbook content:
```bash
# Ensure your Markdown textbook content is placed in a directory, e.g., ./data/textbook_content
docker compose run --rm backend python backend/scripts/ingest.py --input-dir /app/data/textbook_content
```

### 4. Build and Start All Services
```bash
docker compose up --build -d
```

## Usage

### Backend API
The FastAPI backend API will be accessible at `http://localhost:8000/api/v1`. You can access the API documentation (Swagger UI) at `http://localhost:8000/docs`.

### Frontend Chatbot
The Docusaurus frontend with the embedded chatbot will be accessible at `http://localhost:3000`. Interact with the chatbot by typing questions or selecting text on the Docusaurus pages.

## Deployment
Refer to `docs/deployment_guide.md` for detailed deployment instructions and production considerations.

## Contributing
Contributions are welcome! Please refer to our contributing guidelines for more information.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.