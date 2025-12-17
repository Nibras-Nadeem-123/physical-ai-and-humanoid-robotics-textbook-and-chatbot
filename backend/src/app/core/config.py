from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Physical AI Textbook RAG Chatbot"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str = "YOUR_SUPER_SECRET_KEY"  # TODO: Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes

    # Database
    DATABASE_URL: str = "postgresql://user:password@host:port/database"
    
    # Qdrant
    QDRANT_HOST: str = "your-qdrant-cloud-host"
    QDRANT_API_KEY: str = "your-qdrant-api-key"

    # OpenAI
    OPENAI_API_KEY: str = "sk-..."

    # Better Auth
    BETTER_AUTH_API_KEY: str = "your-better-auth-api-key"
    BETTER_AUTH_BASE_URL: str = "http://localhost:8080" # Placeholder

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
