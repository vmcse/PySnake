from collections import deque

class Snake:
    def __init__(self, pos):
        self.body = deque()
        self.body.append(pos)