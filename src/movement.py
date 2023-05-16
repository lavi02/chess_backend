from fastapi import WebSocket


class move:
    def __init__(self) -> None:
        self.white = {}
        self.black = {}
        self.turn = 1

    async def movement_white(self, sio: WebSocket):
        movement = await sio.receive_json()

    async def movement_black(self, sio: WebSocket):
        movement = await sio.receive_json()

        self.turn += 1
