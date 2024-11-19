# app/models/event.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    date = Column(DateTime)
    organizer_id = Column(Integer, ForeignKey("users.id"))
    
    organizer = relationship("CustomUser", back_populates="events")
