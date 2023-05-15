import math
import random


def genRoomId():
    result = ''
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-@"

    for _ in range(16):
        result += seed[math.floor(random.random() * len(seed))]

    return result
