from fastapi import FastAPI
from pydantic import BaseModel
import daysSince

app = FastAPI()

class DaysSince(BaseModel):
    days: int
    color: str

@app.get("/days_since/{date}")
async def get_days_since(date: str):
    days_since = daysSince.calculate(date)
    color = "red" if int(days_since) >= 30 else "black"
    return {"days": f"{days_since}", "color": f"{color}"}