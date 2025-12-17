from typing import Dict, Any

from backend.src.agents.agent_skill import AgentSkill

class ROS2Tutor(AgentSkill):
    @property
    def name(self) -> str:
        return "ROS2 Tutor"

    @property
    def description(self) -> str:
        return "Provides information and tutorials about ROS2 topics."

    async def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder for ROS2-specific logic
        # In a real scenario, this would query a knowledge base,
        # external API, or use a specialized model for ROS2.
        
        if "ros2" in query.lower() or "robot operating system 2" in query.lower():
            return {"output": f"As the ROS2 Tutor, I can help you with your question about ROS2: '{query}'. What specifically about ROS2 are you interested in?", "sources": []}
        else:
            return {"output": "I am the ROS2 Tutor. Please ask me questions related to ROS2.", "sources": []}