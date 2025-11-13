import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Ball Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

platform_x = WIDTH // 2 - 50
platform_y = HEIGHT - 30
platform_width = 100
platform_height = 15
platform_speed = 8

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 15
ball_speed_x = 5
ball_speed_y = 5

score = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x < WIDTH - platform_width:
        platform_x += platform_speed

    # Ball harakati
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Yon devorlarga tegsa
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x *= -1

    # Yuqoriga tegsa
    if ball_y - ball_radius < 0:
        ball_speed_y *= -1

    # Platformaga tegsa
    if (platform_x < ball_x < platform_x + platform_width) and (platform_y < ball_y + ball_radius < platform_y + platform_height):
        ball_speed_y *= -1
        score += 1

    # Pastga tushib ketsa — o'yin tugaydi
    if ball_y > HEIGHT:
        score = 0
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_y = 5

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
































































































































































