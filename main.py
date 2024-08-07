import pygame
from game import Game, Direction
from config import SPEED, WIDTH, HEIGHT, BLOCK_SIZE

SCREEN_HEIGHT = BLOCK_SIZE * HEIGHT + 200
SCREEN_WIDTH = BLOCK_SIZE * WIDTH + BLOCK_SIZE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()
game = Game(WIDTH, HEIGHT)
font = pygame.font.Font("freesansbold.ttf", 40)


def render():
    screen.fill("black")

    pygame.draw.rect(
        screen,
        "gray",
        pygame.Rect(0, 0, SCREEN_WIDTH, HEIGHT * BLOCK_SIZE + BLOCK_SIZE),
    )

    pygame.draw.rect(
        screen,
        "black",
        pygame.Rect(
            BLOCK_SIZE,
            BLOCK_SIZE,
            WIDTH * BLOCK_SIZE - BLOCK_SIZE - 4,
            HEIGHT * BLOCK_SIZE - BLOCK_SIZE - 4,
        ),
    )

    x, y = game.food
    pygame.draw.rect(
        screen,
        "red",
        pygame.Rect(x * HEIGHT, y * WIDTH, BLOCK_SIZE - 4, BLOCK_SIZE - 4),
    )
    for pos in game.snake.body:
        x, y = pos
        pygame.draw.rect(
            screen,
            "white",
            pygame.Rect(x * HEIGHT, y * WIDTH, BLOCK_SIZE - 4, BLOCK_SIZE - 4),
        )

    x, y = game.snake.body[0]
    pygame.draw.rect(
        screen,
        "black",
        pygame.Rect(x * HEIGHT + 5, y * WIDTH + 5, 12, 12),
    )

    if game.pause:
        text = font.render(f"GAME PAUSED", True, "white")
        screen.blit(text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 - 100))
    elif game.game_over:
        text = font.render(f"GAME OVER", True, "white")
        screen.blit(text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 100))

        text = font.render(f"SCORE: {game.score} PRESS F TO TRY AGAIN", True, "white")
        screen.blit(text, (BLOCK_SIZE + 100, SCREEN_HEIGHT - 120))
    else:
        text = font.render(f"SCORE: {game.score}", True, "white")
        screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 120))

    pygame.display.flip()


def handle_key_press():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        game.pause = True
    elif game.game_over and keys[pygame.K_f]:
        game.reset = True
    elif keys[pygame.K_w]:
        game.pause = False
        game.update_direction(Direction.Up)
    elif keys[pygame.K_s]:
        game.pause = False
        game.update_direction(Direction.Down)
    elif keys[pygame.K_a]:
        game.pause = False
        game.update_direction(Direction.Left)
    elif keys[pygame.K_d]:
        game.pause = False
        game.update_direction(Direction.Right)


def main():
    while True:
        clock.tick(SPEED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game.run()
        handle_key_press()
        render()


if __name__ == "__main__":
    main()
    pygame.quit()
