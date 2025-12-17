from typing import Dict, Any, Optional
from pydantic import BaseModel

class AgentSkillBase(BaseModel):
    name: str
    description: Optional[str] = None
    metadata: Dict[str, Any]
    is_active: bool = True

class AgentSkillCreate(AgentSkillBase):
    pass

class AgentSkillResponse(AgentSkillBase):
    id: int

    class Config:
        orm_mode = True
