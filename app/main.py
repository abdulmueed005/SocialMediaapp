from fastapi import FastAPI
import psycopg2
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#the follwing command was needed before alembic gets set up
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#input in origins the list of URLs that can talk to our API. i.e., who can access our api endpoints * for everything
origins =["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#cursor_factor only helps map columns to values. i.e., makes it a nice python dictionary

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello Worlds!!!!!"}


