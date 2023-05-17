import unittest

from src.conn import *
from src.generate_room import *


class testInit(unittest.TestCase):
    def setUp(self):
        self.roomNumber = genRoomId()
