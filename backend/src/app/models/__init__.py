from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class User(BaseModel):
    id: UUID
    auth_id: str
    email: Optional[str] = None
    created_at: datetime
    last_login_at: datetime
    consent_status: bool = False # New field for consent status

class UserInDB(User):
    hashed_password: str

class AgentSkill(BaseModel):
    id: UUID
    name: str
    description: str
    interface_signature: str # Store details about the Python class interface
    activated: bool = True
    created_at: datetime
    last_updated_at: datetime