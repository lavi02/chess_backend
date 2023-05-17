from backend.test.__init__ import testInit


class roomTest(testInit):
    def generateRoomCode(self):
        roomNumLengh = len(self.roomNumber)
        self.assertEqual(roomNumLengh, 16)
