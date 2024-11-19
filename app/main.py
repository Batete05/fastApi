from fastapi import FastAPI
from app.routes import user, event, auth
from app.database import engine
from app import models

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(event.router, prefix="/event", tags=["event"])

models.Base.metadata.create_all(bind=engine)
