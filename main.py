from src.conn import *
from src.routers.generateRoom import *
from src.routers.join import *


@app.websocket("/")
async def endPoint(websocket: WebSocket):
    await connection.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            await websocket.send_text(f"{data}'s number is {connection.connectionTest()}")
    except:
        connection.disconnect(websocket)


@app.websocket("/room/{room_number}")
async def enterRoom(websocket: WebSocket):
    connection
