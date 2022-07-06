from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from database import SessionLocal
from table_user import User
from table_post import Post
from table_feed import Feed
from schema import UserGet, PostGet, FeedGet

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        yield db


@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    try:
        return db.query(User).filter(User.id == id).one()
    except NoResultFound:
        raise HTTPException(404, detail="User not found")

@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    try:
        return db.query(Post).filter(Post.id == id).one()
    except NoResultFound:
        raise HTTPException(404, detail="Post not found")

@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()

@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()

@app.get("/post/recommendations/", response_model=List[PostGet])
def get_post_recommendations(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Post) \
        .join(Feed, Feed.post_id == Post.id) \
        .filter(Feed.action == 'like') \
        .group_by(Post.id) \
        .order_by(func.count(Post.id).desc()) \
        .limit(limit) \
        .all()