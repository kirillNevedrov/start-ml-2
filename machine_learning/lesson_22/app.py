from datetime import datetime
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from schema import PostGet

#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# 

#
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)
#

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        yield db


# @app.get("/user/{id}", response_model=UserGet)
# def get_user(id: int, db: Session = Depends(get_db)):
#     try:
#         return db.query(User).filter(User.id == id).one()
#     except NoResultFound:
#         raise HTTPException(404, detail="User not found")

# @app.get("/post/{id}", response_model=PostGet)
# def get_post(id: int, db: Session = Depends(get_db)):
#     try:
#         return db.query(Post).filter(Post.id == id).one()
#     except NoResultFound:
#         raise HTTPException(404, detail="Post not found")

# @app.get("/user/{id}/feed", response_model=List[FeedGet])
# def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
#     return db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()

# @app.get("/post/{id}/feed", response_model=List[FeedGet])
# def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
#     return db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()

@app.get("/post/recommendations/", response_model=List[PostGet])
def get_post_recommendations(id: int, time: datetime, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Post).limit(limit).all()
    # return db.query(Post) \
    #     .join(Feed, Feed.post_id == Post.id) \
    #     .filter(Feed.action == 'like') \
    #     .group_by(Post.id) \
    #     .order_by(func.count(Post.id).desc()) \
    #     .limit(limit) \
    #     .all()