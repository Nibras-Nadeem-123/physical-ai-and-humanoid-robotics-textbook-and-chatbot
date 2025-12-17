from typing import Annotated

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redislite # Using redislite for an in-memory Redis client for simplicity in development

from backend.src.app.core.dependencies import get_current_user
from backend.src.app.api.endpoints import auth, chat

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Frontend Docusaurus development server
    # Add other frontend origins as needed for production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.on_startup
async def startup():
    # Initialize FastAPILimiter with a redislite client
    # In production, this would be a real Redis instance
    redis_client = redislite.Redis(db=1) # Using a file-based in-memory Redis for dev
    await FastAPILimiter.init(redis_client)
    print("FastAPILimiter initialized with redislite.")


@app.get("/")
async def read_root():
    return {"message": "Physical AI Textbook RAG Chatbot Backend"}

@app.get("/protected", dependencies=[Depends(RateLimiter(times=2, seconds=5))]) # Example rate limit
async def read_protected_route(current_user: Annotated[dict, Depends(get_current_user)], request: Request):
    # The RateLimiter dependency applies rate limiting to this endpoint
    return {"message": f"Hello {current_user['user_id']}, you accessed a protected route! Request from {request.client.host}"}



