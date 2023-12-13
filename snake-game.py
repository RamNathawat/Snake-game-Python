import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SIZE = 20
FPS = 15

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Direction
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid_size = GRID_SIZE
        self.snake_size = SNAKE_SIZE
        self.fps = FPS

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = RIGHT

        self.food = self.generate_food()

    def generate_food(self):
        while True:
            food = (random.randrange(0, self.width, self.grid_size), random.randrange(0, self.height, self.grid_size))
            if food not in self.snake:
                return food

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (*segment, self.snake_size, self.snake_size), border_radius=5)

    def draw_food(self):
        pygame.draw.rect(self.screen, GREEN, (*self.food, self.snake_size, self.snake_size), border_radius=5)

    def move(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0] * self.grid_size, head[1] + self.direction[1] * self.grid_size)
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.screen.fill(BLACK, (*self.snake[-1], self.snake_size, self.snake_size))
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        return (
            head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height or
            head in self.snake[1:]
        )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            self.move()

            if self.check_collision():
                pygame.quit()
                sys.exit()

            self.draw_snake()
            self.draw_food()

            pygame.display.flip()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
