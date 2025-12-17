from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from backend.src.app.core.security import create_access_token
from backend.src.app.services.better_auth import better_auth_client
from backend.src.app.core.dependencies import get_current_user # To get current user id
# from backend.src.app.services.user_service import user_service # Placeholder for user service

router = APIRouter()

class ConsentUpdate(BaseModel):
    consent: bool

@router.post("/login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_data = better_auth_client.authenticate_user(form_data.username, form_data.password)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Here, 'sub' typically represents the user ID. We're getting it from Better Auth's response.
    # We might need to adjust based on actual Better Auth response structure.
    access_token = create_access_token(data={"sub": user_data.get("user_id") or form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/consent")
async def update_user_consent(consent_update: ConsentUpdate, current_user: Annotated[dict, Depends(get_current_user)]):
    user_id = current_user["user_id"]
    # In a real application, you would update the user's consent status in the database here.
    # user_service.update_user_consent(user_id, consent_update.consent)
    print(f"User {user_id} updated consent status to: {consent_update.consent}")
    return {"message": "Consent status updated successfully", "user_id": user_id, "consent": consent_update.consent}