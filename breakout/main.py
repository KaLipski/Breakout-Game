import pygame
import sys
from classes.paddle import Paddle
from classes.ball import Ball
from classes.brick import Brick

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 20
BALL_SIZE = 15
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
PADDLE_Y = SCREEN_HEIGHT - 50
FPS = 90
NUM_BRICKS_X = 10
NUM_BRICKS_Y = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def init_game():
    paddle = Paddle(screen, PADDLE_WIDTH, PADDLE_Y, SCREEN_WIDTH)
    ball = Ball(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SIZE)
    bricks = [Brick(x * BRICK_WIDTH + 5 * (x + 1), y * BRICK_HEIGHT + 5 * (y + 1), BRICK_WIDTH, BRICK_HEIGHT, RED, screen) for x in range(NUM_BRICKS_X) for y in range(NUM_BRICKS_Y)]
    score = 0
    return paddle, ball, bricks, score

# Import and initialize game elements from classes
paddle, ball, bricks, score = init_game()

# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            paddle.move("left")
        if keys[pygame.K_RIGHT]:
            paddle.move("right")

        if ball.update():
            game_over = True

        hit_count = ball.check_collision(paddle, bricks)
        score += hit_count * 10

        # Brick logic handled in Brick class
        bricks = [brick for brick in bricks if not brick.hit(ball.x, ball.y, ball.size)]
        if not bricks:
            game_over = True

        # Drawing
        screen.fill(BLACK)
        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (5, 5))
        pygame.display.flip()
        clock.tick(FPS)
    else:
        # Game Over Display
        end_game_text = font.render(f"GAME OVER! Your Score: {score}", True, WHITE)
        replay_text = font.render("Press Enter to play again", True, WHITE)
        exit_text = font.render("Press Esc to exit", True, WHITE)
        screen.blit(end_game_text, (SCREEN_WIDTH // 2 - end_game_text.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(replay_text, (SCREEN_WIDTH // 2 - replay_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

        if keys[pygame.K_RETURN]:
            paddle, ball, bricks, score = init_game()
            game_over = False
        elif keys[pygame.K_ESCAPE]:
            running = False

pygame.quit()
sys.exit()
