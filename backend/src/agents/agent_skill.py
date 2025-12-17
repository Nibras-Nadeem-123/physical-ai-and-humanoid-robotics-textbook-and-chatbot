from abc import ABC, abstractmethod
from typing import Dict, Any

class AgentSkill(ABC):
    """
    Abstract Base Class for all Agent Skills.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    async def execute(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        pass
