from fastapi import Depends, FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

def get_db():
    return psycopg2.connect("postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml", cursor_factory=RealDictCursor)

@app.get("/user/{id}")
def root(id: str, db = Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT gender, age, city 
            FROM "user"
            WHERE id={id}
            """
        )

        user = cursor.fetchone()

        if user is None:
            raise HTTPException(404, detail="user not found")

        return user