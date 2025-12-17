from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.core.security import create_access_token, verify_password, get_password_hash, get_current_user
from app.models.auth import Token
from app.models.user import User

router = APIRouter()

class ConsentRequest(BaseModel):
    has_consented: bool

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # In a real app, you'd get the user from the database
    # and verify the password against the hashed password.
    # You would also use the Better Auth service to authenticate.
    # For now, we'll use a dummy user and password for demonstration.
    
    # This is a dummy user check.
    # A real implementation would involve a database lookup.
    user_is_valid = (form_data.username == "testuser" and verify_password(form_data.password, get_password_hash("testpassword")))

    if not user_is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": form_data.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.put("/consent", response_model=User)
async def update_consent(consent_request: ConsentRequest, current_user: dict = Depends(get_current_user)):
    # In a real app, you'd get the user from the database
    # and update the consent status.
    # For now, we'll just return a dummy user with the updated consent.
    # This is not a complete implementation.
    
    # Create a user instance from the dictionary
    user = User(id=current_user.get("id", 1), username=current_user.get("username"), has_consented=consent_request.has_consented)
    
    # Here you would save the updated user to the database
    
    return user

