from pydantic import BaseModel
from datetime import datetime

class CreateUser(BaseModel):
    id: int
    email: str
    username: str
    password: str

class CreateBlog(BaseModel):
    id: int
    title: str
    content: str
    author: str
    posted_at: datetime
    user_id: int

class UpdateBlog(BaseModel):
    title: str
    content: str
    updated_at : datetime