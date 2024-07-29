from pydantic import BaseModel
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

