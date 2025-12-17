from typing import List, Dict
from qdrant_client import QdrantClient, models

from backend.src.app.core.config import settings

COLLECTION_NAME = "textbook_chunks"

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(host=settings.QDRANT_HOST, api_key=settings.QDRANT_API_KEY)
        self.vector_size = 1536 # Matches OpenAI's text-embedding-ada-002

    def recreate_collection(self):
        print(f"Recreating Qdrant collection: {COLLECTION_NAME}")
        self.client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=self.vector_size, distance=models.Distance.COSINE),
        )
        print("Collection recreated.")

    def upsert_points(self, points: List[models.PointStruct]):
        print(f"Upserting {len(points)} points to Qdrant collection: {COLLECTION_NAME}")
        self.client.upsert(
            collection_name=COLLECTION_NAME,
            wait=True,
            points=points
        )
        print("Points upserted.")

    def search_points(self, query_vector: List[float], limit: int = 5) -> List[models.ScoredPoint]:
        print(f"Searching Qdrant collection: {COLLECTION_NAME} with limit {limit}")
        search_result = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit,
            with_payload=True
        )
        print(f"Found {len(search_result)} results.")
        return search_result

qdrant_service = QdrantService()
