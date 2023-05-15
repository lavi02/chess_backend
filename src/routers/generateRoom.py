from src.conn import *
from fastapi import Request


@app.get("/api/v1/seed/generate")
async def getRoomNum(user_id: str = ""):
    if (user_id != ""):
        return {"room_number": connection.createRoom(user_id)}
    else:
        return {"error": "wrong parameter"}
