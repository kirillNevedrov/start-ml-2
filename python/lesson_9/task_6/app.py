from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date

app = FastAPI()

@app.post("/user/validate")
def sum_two(user: User) -> str:
    return "ok"