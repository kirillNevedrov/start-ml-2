from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserGet(BaseModel):
    id: int
    age: Optional[int]
    city: Optional[str]
    country: Optional[str]
    exp_group: Optional[int]
    gender: Optional[int]
    os: Optional[str]
    source: Optional[str]

    class Config:
        orm_mode = True

class PostGet(BaseModel):
    id: int
    text: str
    topic: Optional[str]

    class Config:
        orm_mode = True

class FeedGet(BaseModel):
    user_id: Optional[int]
    user: Optional[UserGet]
    post_id: Optional[int]
    post: Optional[PostGet]
    action: Optional[str]
    time: Optional[datetime]

    class Config:
        orm_mode = True
