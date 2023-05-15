from src.conn import *
from pydantic import BaseModel
from typing import Optional


class reqJoinRoomType(BaseModel):
    user_id: str
    room_number: Optional[str] = None


@app.post("/api/v1/join")
async def getRoomNum(req: reqJoinRoomType):
    room = ""
    if req.room_number == None:
        room = connection.getRandomRoom()
    else:
        room = req.room_number
    if room != None:
        connection.joinRoom(room, req.user_id)
        return room


@app.get("/api/v1/room/list")
async def viewRoomNum():
    rooms = connection.getRoomList()
    return rooms
