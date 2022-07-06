from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

@app.get("/user/{id}")
def root(id: str):
    conn = psycopg2.connect("postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT gender, age, city 
        FROM "user"
        WHERE id={id}
        """
    )

    return cursor.fetchone()