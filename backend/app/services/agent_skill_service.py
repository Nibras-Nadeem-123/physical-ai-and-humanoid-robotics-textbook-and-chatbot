from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models import AgentSkill
from app.models.agent_skill import AgentSkillCreate, AgentSkillResponse

class AgentSkillService:
    def get_skill(self, db: Session, skill_id: int) -> Optional[AgentSkill]:
        return db.query(AgentSkill).filter(AgentSkill.id == skill_id).first()

    def get_skill_by_name(self, db: Session, name: str) -> Optional[AgentSkill]:
        return db.query(AgentSkill).filter(AgentSkill.name == name).first()

    def get_skills(self, db: Session, skip: int = 0, limit: int = 100) -> List[AgentSkill]:
        return db.query(AgentSkill).offset(skip).limit(limit).all()

    def create_skill(self, db: Session, skill: AgentSkillCreate) -> AgentSkill:
        db_skill = AgentSkill(
            name=skill.name,
            description=skill.description,
            metadata=skill.metadata,
            is_active=skill.is_active
        )
        db.add(db_skill)
        db.commit()
        db.refresh(db_skill)
        return db_skill
