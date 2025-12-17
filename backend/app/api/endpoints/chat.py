from fastapi import APIRouter, HTTPException, Depends
from backend.app.models.chat import ChatRequest, ChatResponse
from backend.app.services.chat_service import process_chat_message
from backend.app.core.security import get_current_user
from backend.app.models.user import User # Import User model
from fastapi_limiter.depends import RateLimiter

router = APIRouter()

@router.post("/chat", response_model=ChatResponse, dependencies=[Depends(RateLimiter(times=5, seconds=10))])
async def chat(request: ChatRequest, current_user: User = Depends(get_current_user)):
    try:
        result = process_chat_message(
            message=request.query,
            user=current_user
        )
        return ChatResponse(session_id=request.session_id or "default_session", response=result["response"], sources=result["sources"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
