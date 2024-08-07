import random
from enum import Enum
from snake import Snake
from config import BLOCK_SIZE


class Direction(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3


class Game:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.snake = Snake((w // 2, h // 2))
        self.direction = Direction.Up
        self.next_direction = Direction.Up
        self.food = (w - 5, h - 5)
        self.score = 0
        self.pause = True
        self.reset = False
        self.game_over = False

    def update_direction(self, direction):
        if self.game_over or self.pause:
            return

        if (
            (self.direction == Direction.Up and direction == Direction.Up)
            or (self.direction == Direction.Down and direction == Direction.Down)
            or (self.direction == Direction.Right and direction == Direction.Right)
            or (self.direction == Direction.Left and direction == Direction.Left)
            or (self.direction == Direction.Up and direction == Direction.Down)
            or (self.direction == Direction.Down and direction == Direction.Up)
            or (self.direction == Direction.Right and direction == Direction.Left)
            or (self.direction == Direction.Left and direction == Direction.Right)
        ):
            return
        else:
            self.next_direction = direction

    def is_game_over(self, x, y):
        return (
            x >= self.width
            or x < 1
            or y >= self.height
            or y < 1
            or (x, y) in self.snake.body
        )

    def restart(self):
        self.game_over = False
        self.reset = False
        self.score = 0
        self.snake = Snake((self.width // 2, self.height // 2))

    def run(self):
        if self.reset:
            self.restart()
        elif self.game_over or len(self.snake.body) == 0 or self.pause:
            return

        self.direction = self.next_direction

        x, y = self.snake.body[0]

        if self.direction == Direction.Up:
            y -= 1
        elif self.direction == Direction.Down:
            y += 1
        elif self.direction == Direction.Left:
            x -= 1
        elif self.direction == Direction.Right:
            x += 1

        new_head = (x, y)

        if self.is_game_over(x, y):
            self.game_over = True
        else:
            if new_head != self.food:
                self.snake.body.pop()
            else:
                available_spots = []

                for y in range(self.height):
                    for x in range(self.width):
                        if (x, y) not in self.snake.body:
                            if x == 0:
                                x += 1
                            elif y == 0:
                                y += 1
                            pos = (x, y)
                            available_spots.append(pos)
                if len(available_spots) == 0:
                    self.game_over = True
                    return

                self.food = random.choice(available_spots)
                self.score += 1
            self.snake.body.appendleft(new_head)


if __name__ == "__main__":
    game = Game(4, 4)
    game.update_direction(Direction.Down)

    game.run()
    print(game.snake.body)
