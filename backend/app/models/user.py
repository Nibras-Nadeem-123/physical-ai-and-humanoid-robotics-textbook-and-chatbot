from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    has_consented: bool

    class Config:
        orm_mode = True
