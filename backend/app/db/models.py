from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    has_consented = Column(Boolean, default=False)

class AgentSkill(Base):
    __tablename__ = "agent_skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    # Metadata for loading the skill, e.g., module path, class name
    metadata = Column(JSON) 
    is_active = Column(Boolean, default=True)
