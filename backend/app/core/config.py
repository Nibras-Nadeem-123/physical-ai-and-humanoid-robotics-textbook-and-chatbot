from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    QDRANT_HOST: str
    QDRANT_API_KEY: str
    BETTER_AUTH_API_KEY: str
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
