import os
from datetime import datetime
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from catboost import CatBoostClassifier

# from schema import PostGet
import pandas as pd

#
from pydantic import BaseModel


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


#

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


def get_db():
    with SessionLocal() as db:
        yield db


def get_model_path(path: str) -> str:
    if (
        os.environ.get("IS_LMS") == "1"
    ):  # проверяем где выполняется код в лмс, или локально. Немного магии
        MODEL_PATH = "/workdir/user_input/model"
    else:
        MODEL_PATH = path
    return MODEL_PATH


def load_features(user_data, post_text_df, user_id: int, time: datetime):
    # user_data = pd.read_sql(
    #     f"SELECT * FROM user_data WHERE user_id = {user_id}",
    #     SQLALCHEMY_DATABASE_URL
    # )

    # post_text_df = pd.read_sql(
    #     "SELECT * FROM post_text_df",
    #     SQLALCHEMY_DATABASE_URL
    # )

    post_text_df["user_id"] = user_id

    merged_data = pd.merge(
        user_data[user_data["user_id"] == user_id],
        post_text_df,
        how="outer",
        on="user_id",
    )

    data = merged_data.dropna()

    data["user_id"] = data["user_id"].astype(str)
    data["gender"] = data["gender"].astype(str)
    data["age"] = data["age"].astype(str)
    data["exp_group"] = data["exp_group"].astype(str)
    data["post_id"] = data["post_id"].astype(str)
    data["timestamp"] = time.isoformat()

    return data


def load_models():
    model_path = get_model_path(
        "C:\Git\start-ml-2\machine_learning\lesson_22\catboost_model.cbm"
    )
    model = CatBoostClassifier()
    model.load_model(model_path)
    return model


app = FastAPI()


model = load_models()

user_data_orig = pd.read_sql(f"SELECT * FROM user_data", SQLALCHEMY_DATABASE_URL)

post_text_df_orig = pd.read_sql("SELECT * FROM post_text_df", SQLALCHEMY_DATABASE_URL)


@app.get("/post/recommendations/", response_model=List[PostGet])
def get_post_recommendations(
    id: int, time: datetime, limit: int = 10, db: Session = Depends(get_db)
):
    features = load_features(
        user_data=user_data_orig, post_text_df=post_text_df_orig, user_id=id, time=time
    )
    features["predict_proba"] = model.predict_proba(features)[:, 1]
    return (
        features.sort_values(by=["predict_proba"], ascending=False)
        .head(limit)[["post_id", "text", "topic"]]
        .rename(columns={"post_id": "id"})
        .to_dict("records")
    )
    # return db.query(Post).limit(limit).all()
    # return db.query(Post) \
    #     .join(Feed, Feed.post_id == Post.id) \
    #     .filter(Feed.action == 'like') \
    #     .group_by(Post.id) \
    #     .order_by(func.count(Post.id).desc()) \
    #     .limit(limit) \
    #     .all()
