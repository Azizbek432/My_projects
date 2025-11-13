import pygame
import sys
import random

pygame.init()
# Oyna o'lchami
KENGLIK, BALANDLIK = 600, 300
ekran = pygame.display.set_mode((KENGLIK, BALANDLIK))
pygame.display.set_caption("Dino O'yini")
# Ranglar
OQ = (255, 255, 255)
QORA = (0, 0, 0)
USTUN_RANGI = (200, 0, 0)
soat = pygame.time.Clock()

# Dinozavr rasmni yuklash
dino_rasm = pygame.image.load("images/dino.png")
dino_rasm = pygame.transform.scale(dino_rasm, (40, 40))

# Dinozavr parametrlari
dino_x = 50
dino_y = BALANDLIK - 60
dino_kenglik = 40
dino_balandlik = 40
sakrash = False
sakrash_balandligi = 10
tezlik = sakrash_balandligi

# Ustun parametrlari
ustun_kenglik = 10
ustun_balandlik = random.randint(20, 40)
ustun_x = KENGLIK
ustun_y = BALANDLIK - ustun_balandlik - 20
ustun_tezlik = 7

ball = 0

while True:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if hodisa.type == pygame.KEYDOWN:
            if hodisa.key == pygame.K_SPACE and not sakrash:
                sakrash = True

    # Dinozavr sakrashi
    if sakrash:
        dino_y -= tezlik
        tezlik -= 1
        if tezlik < -sakrash_balandligi:
            sakrash = False
            tezlik = sakrash_balandligi

    # Ustun harakati va ball
    ustun_x -= ustun_tezlik
    if ustun_x < -ustun_kenglik:
        ustun_x = KENGLIK
        ustun_balandlik = random.randint(20, 40)
        ustun_y = BALANDLIK - ustun_balandlik - 20
        ball += 1

    # To'qnashuvni tekshirish
    dino_rect = pygame.Rect(dino_x, dino_y, dino_kenglik, dino_balandlik)
    ustun_rect = pygame.Rect(ustun_x, ustun_y, ustun_kenglik, ustun_balandlik)
    if dino_rect.colliderect(ustun_rect):
        print("O'yin tugadi! Ball:", ball)
        pygame.quit()
        sys.exit()

    # Chizish
    ekran.fill(OQ)
    ekran.blit(dino_rasm, (dino_x, dino_y))
    pygame.draw.rect(ekran, USTUN_RANGI, ustun_rect)

    # Ballni chiqarish
    shrift = pygame.font.SysFont(None, 36)
    ball_matni = shrift.render(f"Ball: {ball}", True, QORA)
    ekran.blit(ball_matni, (10, 10))

    pygame.display.flip()
    soat.tick(60)