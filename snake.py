import pygame
import sys
import random


def game_over():
    font = pygame.font.SysFont(None, 60)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(
        text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2)
    )
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


pygame.init()

width = 600
height = 400

snake = [(100, 100), (90, 100), (80, 100)]
snake_size = 10

direction = "RIGHT"
speed = 10

food = (random.randrange(0, width, 10), random.randrange(0, height, 10))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    head_x, head_y = snake[0]

    if direction == "RIGHT":
        head_x += speed
    elif direction == "LEFT":
        head_x -= speed
    elif direction == "UP":
        head_y -= speed
    elif direction == "DOWN":
        head_y += speed

    snake.insert(0, (head_x, head_y))

    if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
        game_over()

    if (head_x, head_y) in snake[1:]:
        game_over()

    if snake[0] == food:
        food = (random.randrange(0, width, 10), random.randrange(0, height, 10))
    else:
        snake.pop()

    screen.fill((0, 0, 0))

    for segment in snake:
        pygame.draw.rect(
            screen, (0, 255, 0), (segment[0], segment[1], snake_size, snake_size)
        )

    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], snake_size, snake_size))

    pygame.display.update()
    clock.tick(10)
