import random
import pygame
import sys
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        x_pos = cell_size * self.pos.x
        y_pos = cell_size * self.pos.y
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 114, 115), fruit_rect)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            # create a rect
            snake_block = pygame.Rect(cell_size * block.x, cell_size * block.y, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 50, 122), snake_block)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.body.insert(0, self.body[0] + self.direction)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = FRUIT()
            self.snake.add_block()

pygame.init()
cell_size = 20
cell_number = 40
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number), vsync=1)
clock = pygame.time.Clock()

main_game = MAIN()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
    screen.fill((134, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(144)
