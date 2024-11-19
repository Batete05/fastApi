# app/schemas/user.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "volunteer"

    class Config:
        orm_mode = True
