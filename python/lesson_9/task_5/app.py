from datetime import date, timedelta
from fastapi import FastAPI

app = FastAPI()

@app.get("/sum_date")
def sum_two(current_date : date, offset: int) -> date:
    return current_date + timedelta(days=offset)