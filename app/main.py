from fastapi import Body, FastAPI, Depends, status
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from pydantic import BaseSettings
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# path operation
@app.get("/")
def root():
    return {"message": "Hey Tribal Brethren, welcome to my api!!!"}
