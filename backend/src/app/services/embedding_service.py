import os
from typing import List
from openai import OpenAI

from backend.src.app.core.config import settings

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "text-embedding-ada-002" # Based on research.md
        self.embedding_dimensions = 1536 # Expected dimensions for this model

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        try:
            response = self.client.embeddings.create(input=texts, model=self.model)
            return [data.embedding for data in response.data]
        except Exception as e:
            print(f"Error getting embeddings from OpenAI: {e}")
            # Fallback to dummy or raise exception based on error handling strategy
            return [[0.0] * self.embedding_dimensions for _ in texts] # Dummy fallback

embedding_service = EmbeddingService()
