from src.conn import *
from src.routers.generateRoom import *
from src.routers.join import *
from src.routers.user import *
from src.routers.room import *
from src.routers.generateRoom import *
from src.movement import *


@app.websocket("/")
async def endPoint(websocket: WebSocket):
    await connection.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            await websocket.send_text(f"{data}'s number is {connection.connectionTest()}")
    except:
        connection.disconnect(websocket)
