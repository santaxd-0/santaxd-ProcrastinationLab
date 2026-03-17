from fastapi import FastAPI, HTTPException
from datetime import datetime

from enums.mood_enum import MoodEnum
from custom_types.sponge_type import SPONGE_TYPE

app = FastAPI()

@app.get("/sponge")
async def sponge_meme(text: SPONGE_TYPE = None):
    if text:
        return_mem_string: str = ""
        for index, symbol in enumerate(text):
            if (index % 2 != 0 and symbol != " "):
                return_mem_string += symbol.upper()
            else:
                return_mem_string += symbol
        return {
            "message": f"Here`s your meme text: {return_mem_string}"
        }
    return {
        "message": "Try by entering some cool text in ?text= query"
    }

@app.get("/today")
async def get_mood_today():
    today = datetime.now().strftime("%A").lower()
    try:
        mood_key = f"{today}Mood"
        return {"mood": MoodEnum[mood_key]}
    except KeyError:
        raise HTTPException(status_code=404, detail="Такого дня нет. Ты живёшь вне времени.")


@app.get("/{day}")
async def get_mood(day: str):
    try:
        mood_key = f"{day}Mood"
        return {"mood": MoodEnum[mood_key]}
    except KeyError:
        raise HTTPException(status_code=404, detail="Такого дня нет. Ты живёшь вне времени.")