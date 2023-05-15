import random

from typing import List
from fastapi import FastAPI, WebSocket

from .generate_room import *

app = FastAPI()


class manageConn:
    def __init__(self):
        self.emptyRoom = {}
        self.fullRoom = {}

        self.active_connections: List[WebSocket] = []

    async def connect(self, sio: WebSocket):
        await sio.accept()
        self.active_connections.append(sio)

    def disconnect(self, sio: WebSocket):
        self.active_connections.remove(sio)

    def createRoom(self, userid: str):
        roomNum = genRoomId()
        self.emptyRoom[roomNum] = userid

        return roomNum

    def getRandomRoom(self):
        if len(self.emptyRoom) != 0:
            return random.choice(list(self.emptyRoom.keys()))
        else:
            return None

    def getRoomList(self):
        print(f"{self.emptyRoom} => 빈 방")
        print(f"{self.fullRoom} => 찬 방")

        return self.fullRoom

    def joinRoom(self, seed: str, userid: str):
        if seed not in self.fullRoom:
            self.fullRoom[seed] = {
                "count": 2, "users": [self.emptyRoom[seed], userid], "viewers": []
            }
            del self.emptyRoom[seed]

        else:
            self.fullRoom[seed]["count"] += 1
            self.fullRoom[seed]["viewers"].append(userid)

        print(f"{self.emptyRoom} => 빈 방")
        print(f"{self.fullRoom} => 찬 방")

    def leftRoom(self, seed: str, userid: str):
        if seed in self.emptyRoom:
            del self.emptyRoom[seed]
        else:
            if userid in self.fullRoom[seed]["users"]:
                del self.fullRoom[seed]
            else:
                self.fullRoom[seed]["viewers"].remove(userid)


connection = manageConn()
