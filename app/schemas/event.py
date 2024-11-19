# app/schemas/event.py
from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    description: str
    date: datetime

    class Config:
        orm_mode = True
