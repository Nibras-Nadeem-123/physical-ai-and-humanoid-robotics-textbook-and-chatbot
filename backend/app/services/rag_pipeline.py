from typing import List, Dict

from app.services.embedding_service import EmbeddingService
from app.services.qdrant_service import QdrantService
from app.services.generative_service import GenerativeService

class RAGPipeline:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_service = QdrantService()
        self.generative_service = GenerativeService()

    def run_pipeline(self, query: str) -> Dict:
        # 1. Embed the query
        query_vector = self.embedding_service.get_embeddings([query])[0]

        # 2. Retrieve relevant chunks from Qdrant
        retrieved_chunks = self.qdrant_service.search_vectors(query_vector)

        # 3. Generate response using the generative model
        response_content = self.generative_service.generate_response(query, retrieved_chunks)

        # 4. Format generated answers with plain text references
        formatted_response = response_content
        if retrieved_chunks:
            source_refs = [chunk["source_ref"] for chunk in retrieved_chunks]
            formatted_response += "\n\nSources: " + ", ".join(source_refs)

        return {
            "response": formatted_response,
            "sources": [chunk["source_ref"] for chunk in retrieved_chunks]
        }
