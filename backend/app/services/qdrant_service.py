from typing import List, Dict

from qdrant_client import QdrantClient, models

from app.core.config import settings

COLLECTION_NAME = "textbook_chunks"

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(host=settings.QDRANT_HOST, api_key=settings.QDRANT_API_KEY)

    def search_vectors(self, query_vector: List[float], top_k: int = 5) -> List[Dict]:
        search_result = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=top_k,
            append_payload=True
        )
        return [{"content": hit.payload["content"], "source_ref": hit.payload["source_ref"]} for hit in search_result]
