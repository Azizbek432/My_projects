import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini milta (Arkanoid)")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

platform_x = WIDTH // 2 - 50
platform_y = HEIGHT - 30
platform_width = 100
platform_height = 15
platform_speed = 8

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 12
ball_speed_x = 5
ball_speed_y = -5

# Bloklar (tepadan bir necha qator)
blocks = []
block_rows = 5
block_cols = 8
block_width = 55
block_height = 20
for row in range(block_rows):
    for col in range(block_cols):
        blocks.append(pygame.Rect(10 + col * (block_width + 5), 40 + row * (block_height + 5), block_width, block_height))

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

    # Bloklarga tegsa
    hit_index = ball_rect = None
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    for i, block in enumerate(blocks):
        if ball_rect.colliderect(block):
            ball_speed_y *= -1
            score += 1
            del blocks[i]
            break

    # Pastga tushib ketsa — o'yin tugaydi
    if ball_y > HEIGHT:
        score = 0
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_y = -5
        blocks = []
        for row in range(block_rows):
            for col in range(block_cols):
                blocks.append(pygame.Rect(10 + col * (block_width + 5), 40 + row * (block_height + 5), block_width, block_height))

    # G‘alaba sharti
    if not blocks:
        font = pygame.font.SysFont(None, 48)
        win_text = font.render("You Win!", True, GREEN)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2 - 24))
        pygame.display.flip()
        pygame.time.wait(2000)
        # O'yinni qayta boshlash
        score = 0
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_y = -5
        blocks = []
        for row in range(block_rows):
            for col in range(block_cols):
                blocks.append(pygame.Rect(10 + col * (block_width + 5), 40 + row * (block_height + 5), block_width, block_height))

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
