from typing import List, Any, Dict
from qdrant_client.http.models import ScoredPoint
from openai import OpenAI

from backend.src.app.core.config import settings
from backend.src.app.services.embedding_service import embedding_service
from backend.src.app.services.qdrant_service import qdrant_service

class RAGService:
    def __init__(self):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service
        self.openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.generation_model = "gpt-3.5-turbo" # Or gpt-4, depending on preference/cost

    def get_query_embedding(self, query: str) -> List[float]:
        return self.embedding_service.get_embeddings([query])[0]

    def retrieve_chunks(self, query_vector: List[float], limit: int = 5) -> List[ScoredPoint]:
        return self.qdrant_service.search_points(query_vector, limit=limit)

    def generate_response(self, query: str, retrieved_chunks: List[ScoredPoint]) -> Dict[str, Any]:
        context_text = "\n\n".join([chunk.payload["content"] for chunk in retrieved_chunks if chunk.payload])
        
        messages = [
            {"role": "system", "content": "You are a helpful assistant for a Physical AI & Humanoid Robotics textbook. Answer questions based only on the provided context from the textbook. If you cannot find the answer in the context, state that you cannot answer the question based on the provided information."},
            {"role": "user", "content": f"Context from textbook:\n{context_text}\n\nQuestion: {query}"}
        ]

        try:
            response = self.openai_client.chat.completions.create(
                model=self.generation_model,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            answer = response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response from OpenAI: {e}")
            answer = "I apologize, but I am currently unable to generate a response."

        citations = [chunk.payload["source_ref"] for chunk in retrieved_chunks if chunk.payload and "source_ref" in chunk.payload]
        
        return {"answer": answer, "citations": citations}

rag_service = RAGService()

