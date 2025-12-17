import importlib
from typing import Dict, Any

from app.db.database import get_db
from app.db.models import AgentSkill as AgentSkillDB
from app.services.agent_skill_service import AgentSkillService
from backend.src.agents.agent_skill import AgentSkill # Import the interface

class AgentOrchestrator:
    def __init__(self):
        self.agent_skill_service = AgentSkillService()
        self.loaded_skills: Dict[str, AgentSkill] = {}

    async def _load_skill(self, skill_metadata: Dict[str, Any]) -> AgentSkill:
        module_path = skill_metadata["module_path"]
        class_name = skill_metadata["class_name"]

        module = importlib.import_module(module_path)
        skill_class = getattr(module, class_name)
        
        # Instantiate the skill
        skill_instance = skill_class()
        return skill_instance

    async def orchestrate(self, query: str, user_context: Dict) -> Dict:
        # For demonstration, let's load all active skills and try to use them
        db = next(get_db()) # Get a database session
        active_skills_db = self.agent_skill_service.get_skills(db, is_active=True) # Assuming is_active filter
        db.close()

        for skill_db in active_skills_db:
            if skill_db.name not in self.loaded_skills:
                self.loaded_skills[skill_db.name] = await self._load_skill(skill_db.metadata)
            
            skill_instance = self.loaded_skills[skill_db.name]
            # Simple routing: if query contains skill name, execute it
            if skill_instance.name.lower() in query.lower():
                result = await skill_instance.execute(query, user_context)
                return {"response": f"Agent {skill_instance.name} used: {result['output']}", "agent_used": skill_instance.name}
        
        return {"response": f"No specific agent found for query: {query}", "agent_used": "RAG"} # Fallback to RAG