from app.models.user import User
from app.services.rag_pipeline import RAGPipeline

rag_pipeline = RAGPipeline()

def process_chat_message(message: str, user: User):
    if not user.has_consented:
        return {"response": "I cannot process your request without your consent to our data usage policy.", "sources": []}
    
    response = rag_pipeline.run_pipeline(message)
    return response
