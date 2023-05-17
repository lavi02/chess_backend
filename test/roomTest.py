from backend.test.__init__ import testInit
from src.conn import *
from fastapi.testclient import TestClient

client = TestClient(app)


class roomTest(testInit):
    def generateRoomCode(self):
        roomNumLengh = len(self.roomNumber)
        self.assertEqual(roomNumLengh, 16)

    def readRoomNum(self):
        res = client.get("/api/v1/seed/generate")
        self.assertEqual(res.status_code == 201)
        self.assertEqual(res.json() == {"room_number": ""})
