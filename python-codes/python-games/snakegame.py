import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def draw_rect(color, pos):
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def random_position():
    return [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

def main():
    snake = [[5, 5]]
    direction = [1, 0]
    food = random_position()
    score = 0

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction[1] != 1:
                    direction = [0, -1]
                elif event.key == pygame.K_DOWN and direction[1] != -1:
                    direction = [0, 1]
                elif event.key == pygame.K_LEFT and direction[0] != 1:
                    direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and direction[0] != -1:
                    direction = [1, 0]

        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        if head in snake or head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            break

        snake.insert(0, head)

        if head == food:
            food = random_position()
            score += 1
        else:
            snake.pop()

        draw_rect(RED, food)
        for segment in snake:
            draw_rect(GREEN, segment)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

    game_over_text = font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)

main()

