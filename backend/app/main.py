from fastapi import FastAPI
from backend.app.database import engine
from backend.app.models import Base
from backend.app.auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(auth_router)