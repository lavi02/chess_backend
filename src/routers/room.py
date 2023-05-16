from src.conn import *
from pydantic import BaseModel
from typing import Optional


@app.get("/room/{room_number}/movement")
async def checkMovement(room_number):
    pass
