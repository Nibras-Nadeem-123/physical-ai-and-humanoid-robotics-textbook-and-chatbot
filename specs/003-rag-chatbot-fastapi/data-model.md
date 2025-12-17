# Data Model for Physical AI Textbook RAG Chatbot

This document describes the key entities and their attributes for the "Physical AI Textbook RAG Chatbot" project.

## Entities

### User

Represents an individual interacting with the chatbot.

-   **id** (UUID): Unique identifier for the user.
-   **auth_id** (String): Identifier from the "Better Auth" service.
-   **email** (String): User's email address (optional, based on privacy settings).
-   **created_at** (DateTime): Timestamp of user creation.
-   **last_login_at** (DateTime): Timestamp of last user login.

### Conversation

Represents a continuous chat session between a user and the chatbot.

-   **id** (UUID): Unique identifier for the conversation.
-   **user_id** (UUID): Foreign key referencing the `User` entity.
-   **started_at** (DateTime): Timestamp when the conversation began.
-   **last_updated_at** (DateTime): Timestamp of the last message in the conversation.

### Message

Represents a single turn in a conversation, either from the user or the chatbot.

-   **id** (UUID): Unique identifier for the message.
-   **conversation_id** (UUID): Foreign key referencing the `Conversation` entity.
-   **sender** (Enum: 'user', 'chatbot'): Indicates who sent the message.
-   **text** (String): The content of the message.
-   **context** (JSON, optional): Additional context about the message, e.g., selected text for user queries.
-   **timestamp** (DateTime): When the message was sent.
-   **citations** (JSON Array, optional): Array of references if the message is from the chatbot (FR-012).

### TextChunk

Represents a semantically meaningful segment of the textbook content.

-   **id** (UUID): Unique identifier for the chunk.
-   **text** (String): The actual text content of the chunk.
-   **embedding** (Vector): The vector representation of the text chunk. Stored in Qdrant.
-   **source_ref** (String): Reference to the original location in the textbook (e.g., "Chapter 1, Section 2.3").
-   **document_id** (UUID): Foreign key referencing the `Document` entity.
-   **created_at** (DateTime): Timestamp of chunk creation/ingestion.

### Document

Represents a processed textbook document or part of it.

-   **id** (UUID): Unique identifier for the document.
-   **title** (String): Title of the document (e.g., "Physical AI Textbook - Chapter 1").
-   **file_path** (String): Original file path of the Markdown document.
-   **ingested_at** (DateTime): Timestamp of when the document was ingested.

### AgentSkill

Metadata for a reusable skill that the agent can invoke.

-   **id** (UUID): Unique identifier for the skill.
-   **name** (String): Unique name of the skill (e.g., "ROS2_Tutor").
-   **description** (String): A brief description of what the skill does.
-   **interface_signature** (String): Description of the Python class interface (e.g., method names, expected arguments).
-   **activated** (Boolean): Whether the skill is currently active/enabled.
-   **created_at** (DateTime): Timestamp of skill definition.
-   **last_updated_at** (DateTime): Timestamp of last update to skill definition.