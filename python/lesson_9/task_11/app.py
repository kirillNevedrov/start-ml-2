from fastapi import Depends, FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

app = FastAPI()

def get_db():
    return psycopg2.connect("postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml", cursor_factory=RealDictCursor)

@app.get("/post/{id}", response_model=PostResponse)
def root(id: str, db = Depends(get_db)) -> PostResponse:
    with db.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT id, text, topic 
            FROM "post"
            WHERE id={id}
            """
        )

        post = cursor.fetchone()

        if post is None:
            raise HTTPException(404, detail="post not found")

        return PostResponse(**post)