import openai
from typing import List

from app.core.config import settings

class EmbeddingService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(
            input=texts,
            model="text-embedding-ada-002"
        )
        return [item['embedding'] for item in response['data']]
