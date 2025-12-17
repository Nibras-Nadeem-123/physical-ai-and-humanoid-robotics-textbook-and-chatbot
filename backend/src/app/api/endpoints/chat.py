from typing import Annotated, Optional, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

from backend.src.app.core.dependencies import get_current_user
from backend.src.app.services.rag_service import rag_service
from backend.src.app.services.user_service import user_service # Assuming user service is needed for consent check

router = APIRouter()

class ChatQuery(BaseModel):
    query: str = Field(..., min_length=1, max_length=500, description="The user's question.")
    context: Optional[str] = Field(None, max_length=1000, description="Optional selected text context for the query.")

class ChatResponse(BaseModel):
    answer: str
    citations: List[str]

@router.post("/chat", response_model=ChatResponse)
async def chat_with_rag(
    chat_query: ChatQuery,
    current_user: Annotated[dict, Depends(get_current_user)]
):
    user_id = current_user["user_id"]
    # In a real app, fetch user details including consent status
    # For now, let's assume we have the consent status from user_service or similar
    # Placeholder: user = user_service.get_user_by_id(user_id)
    # user_consent = user.consent_status if user else False

    # Simulate fetching user consent status for demonstration
    # This `NEEDS CLARIFICATION` will need to be properly integrated with user_service
    # and possibly frontend consent flow.
    user_consent = True # For now, assume consented to proceed with chat

    if not user_consent:
        # This check aligns with the "Ensure data processing adheres to user consent status" task (E3 remediation)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User consent required for data processing."
        )

    # 1. Embed Query
    query_vector = rag_service.get_query_embedding(chat_query.query)

    # 2. Retrieve Chunks
    # If context is provided (selected text), we might adjust retrieval logic here
    retrieved_chunks = rag_service.retrieve_chunks(query_vector) # Basic retrieval for now

    # 3. Generate Response
    response_data = rag_service.generate_response(chat_query.query, retrieved_chunks)

    return ChatResponse(answer=response_data["answer"], citations=response_data["citations"])
