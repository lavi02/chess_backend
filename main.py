from src.conn import *
from src.routers.generateRoom import *
from src.routers.join import *


@app.websocket("/")
async def endPoint(websocket: WebSocket):
    await connection.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()

            await websocket.send_text(f"{data['data']}'s room number is {connection.room_number()}")
    except:
        connection.disconnect(websocket)


@app.websocket("/room/{room_number}")
async def enterRoom(websocket: WebSocket):
    connection
