# main.py
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from app import utils
import time
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
import app.models as models
from app.schemas import PostSchema, PostCreate, Post, UserCreate, UserOut
from .routers import post, user, auth
models.Base.metadata.create_all(bind=engine)

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost', 
            database='fastapi',
            user='postgres', 
            password='Postgres@123',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Error while connecting to database, Error: ", error)
        time.sleep(2)


my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1}, 
    {"title": "favorite foods", "content": "I like pizza", "id": 2}
]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello world!"}




