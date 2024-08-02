from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostSchema):
    pass

class Post(PostSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True


class userLogin(BaseModel):
    email: EmailStr
    password: str