import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player_x = WIDTH // 2 - 20
player_y = HEIGHT - 60
player_speed = 7

bullets = []
enemies = [pygame.Rect(random.randint(0, WIDTH - 40), random.randint(-150, -40), 40, 40) for _ in range(3)]
enemy_speed = 2
score = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player_x + 15, player_y, 10, 20))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 40:
        player_x += player_speed

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0, WIDTH - 40)
            enemy.y = random.randint(-150, -40)

    # Collision detection
    for bullet in bullets[:]:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                score += 1
                if bullet in bullets:
                    bullets.remove(bullet)
                enemy.x = random.randint(0, WIDTH - 40)
                enemy.y = random.randint(-150, -40)

    screen.fill(WHITE)
    player_rect = pygame.Rect(player_x, player_y, 40, 40)
    pygame.draw.rect(screen, BLUE, player_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, enemy)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)