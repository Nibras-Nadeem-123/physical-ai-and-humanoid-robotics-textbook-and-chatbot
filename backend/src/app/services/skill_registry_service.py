from typing import Dict, Any, Optional
from uuid import UUID, uuid4
from datetime import datetime

from backend.src.app.models import AgentSkill
from typing import List # Added for get_all_active_skills

# In-memory mock registry for demonstration
_mock_skill_registry: Dict[UUID, AgentSkill] = {}

class SkillRegistryService:
    def register_skill(self, name: str, description: str, interface_signature: str) -> AgentSkill:
        skill_id = uuid4()
        new_skill = AgentSkill(
            id=skill_id,
            name=name,
            description=description,
            interface_signature=interface_signature,
            activated=True,
            created_at=datetime.utcnow(),
            last_updated_at=datetime.utcnow()
        )
        _mock_skill_registry[skill_id] = new_skill
        return new_skill

    def get_skill_by_name(self, name: str) -> Optional[AgentSkill]:
        for skill in _mock_skill_registry.values():
            if skill.name == name:
                return skill
        return None
    
    def get_all_active_skills(self) -> List[AgentSkill]:
        return [skill for skill in _mock_skill_registry.values() if skill.activated]

skill_registry_service = SkillRegistryService()

# Pre-register some dummy skills for testing agent orchestrator
skill_registry_service.register_skill(
    name="ROS2_Tutor",
    description="Provides detailed information and tutorials on ROS2.",
    interface_signature="backend.src.agents.ros2_tutor.ROS2_Tutor"
)

skill_registry_service.register_skill(
    name="Humanoid_Control_Expert",
    description="Answers questions related to humanoid robot control and kinematics.",
    interface_signature="backend.src.agents.humanoid_control_expert.Humanoid_Control_Expert"
)