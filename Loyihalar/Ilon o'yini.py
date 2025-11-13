import pygame
import sys
import random

pygame.init()
KENGLIK, BALANDLIK = 600, 500
HUJAYRA = 20
ekran = pygame.display.set_mode((KENGLIK, BALANDLIK))
pygame.display.set_caption("Ilon O'yini")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

ilon = [(100, 100), (80, 100), (60, 100)]
yo_nalish = (HUJAYRA, 0)
meva = (random.randrange(0, KENGLIK, HUJAYRA), random.randrange(0, BALANDLIK, HUJAYRA))
ball = 0
tezlik = 10

soat = pygame.time.Clock()

def ilonni_harakatlantir(ilon, yo_nalish):
    bosh = (ilon[0][0] + yo_nalish[0], ilon[0][1] + yo_nalish[1])
    ilon.insert(0, bosh)
    return ilon

def toqnashuvni_tekshir(ilon):
    bosh = ilon[0]
    if (bosh[0] < 0 or bosh[0] >= KENGLIK or bosh[1] < 0 or bosh[1] >= BALANDLIK or bosh in ilon[1:]):
        return True
    return False

def game_over(ball):
    shrift = pygame.font.SysFont(None, 48)
    matn = shrift.render(f"O'yin tugadi! Ball: {ball}", True, RED)
    ekran.blit(matn, (KENGLIK // 2 - 150, BALANDLIK // 2 - 24))
    pygame.display.flip()
    pygame.time.wait(2000)

while True:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif hodisa.type == pygame.KEYDOWN:
            if hodisa.key == pygame.K_UP and yo_nalish != (0, HUJAYRA):
                yo_nalish = (0, -HUJAYRA)
            elif hodisa.key == pygame.K_DOWN and yo_nalish != (0, -HUJAYRA):
                yo_nalish = (0, HUJAYRA)
            elif hodisa.key == pygame.K_LEFT and yo_nalish != (HUJAYRA, 0):
                yo_nalish = (-HUJAYRA, 0)
            elif hodisa.key == pygame.K_RIGHT and yo_nalish != (-HUJAYRA, 0):
                yo_nalish = (HUJAYRA, 0)

    ilon = ilonni_harakatlantir(ilon, yo_nalish)

    # Meva yeb qo'yilsa
    if ilon[0] == meva:
        ball += 1
        tezlik = 10  # Tezlikni 5 dan oshirmang
        meva = (random.randrange(0, KENGLIK, HUJAYRA), random.randrange(0, BALANDLIK, HUJAYRA))
    else:
        ilon.pop()

    if toqnashuvni_tekshir(ilon):
        game_over(ball)
        # O'yinni qayta boshlash
        ilon = [(100, 100), (80, 100), (60, 100)]
        yo_nalish = (HUJAYRA, 0)
        meva = (random.randrange(0, KENGLIK, HUJAYRA), random.randrange(0, BALANDLIK, HUJAYRA))
        ball = 0
        tezlik = 10

    ekran.fill(BLACK)
    for i, qism in enumerate(ilon):
        if i == 0:
            pygame.draw.rect(ekran,GREEN, (*qism, HUJAYRA, HUJAYRA))
            pygame.draw.circle(ekran,WHITE , (qism[0] + 5, qism[1] + 6), 3)
            pygame.draw.circle(ekran, WHITE, (qism[0] + HUJAYRA - 5, qism[1] + 6), 3)
            pygame.draw.circle(ekran, BLACK, (qism[0] + 5, qism[1] + 6), 1)
            pygame.draw.circle(ekran,BLACK, (qism[0] + HUJAYRA - 5, qism[1] + 6), 1)
        else:
            pygame.draw.rect(ekran, GREEN, (*qism, HUJAYRA, HUJAYRA))
    pygame.draw.rect(ekran, RED, (*meva, HUJAYRA, HUJAYRA))

    shrift = pygame.font.SysFont(None, 36)
    ball_matni = shrift.render(f"Ball: {ball}", True, WHITE)
    ekran.blit(ball_matni, (10, 10))

    pygame.display.flip()
    soat.tick(tezlik) 
import sys
import random

pygame.init()
KENGLIK, BALANDLIK = 400, 400
HUJAYRA = 20
ekran = pygame.display.set_mode((KENGLIK, BALANDLIK))
pygame.display.set_caption("Ko'zli Ilon O'yini")

QORA = (0, 0, 0)
YASHIL = (0, 255, 0)
QIZIL = (255, 0, 0)
OQ = (255, 255, 255)

ilon = [(100, 100), (80, 100), (60, 100)]
yo_nalish = (HUJAYRA, 0)
meva = (random.randrange(0, KENGLIK, HUJAYRA), random.randrange(0, BALANDLIK, HUJAYRA))
ball = 0
tezlik = 10

soat = pygame.time.Clock()

def ilonni_harakatlantir(ilon, yo_nalish):
    bosh = (ilon[0][0] + yo_nalish[0], ilon[0][1] + yo_nalish[1])
    ilon.insert(0, bosh)
    return ilon

def toqnashuvni_tekshir(ilon):
    bosh = ilon[0]
    if (bosh[0] < 0 or bosh[0] >= KENGLIK or bosh[1] < 0 or bosh[1] >= BALANDLIK or bosh in ilon[1:]):
        return True
    return False

def game_over(ball):
    shrift = pygame.font.SysFont(None, 48)
    matn = shrift.render(f"O'yin tugadi! Ball: {ball}", True, QIZIL)
    ekran.blit(matn, (KENGLIK // 2 - 150, BALANDLIK // 2 - 24))
    pygame.display.flip()
    pygame.time.wait(2000)

while True:
    for hodisa in pygame.event.get():
        if hodisa.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif hodisa.type == pygame.KEYDOWN:
            if hodisa.key == pygame.K_UP and yo_nalish != (0, HUJAYRA):
                yo_nalish = (0, -HUJAYRA)
            elif hodisa.key == pygame.K_DOWN and yo_nalish != (0, -HUJAYRA):
                yo_nalish = (0, HUJAYRA)
            elif hodisa.key == pygame.K_LEFT and yo_nalish != (HUJAYRA, 0):
                yo_nalish = (-HUJAYRA, 0)
            elif hodisa.key == pygame.K_RIGHT and yo_nalish != (-HUJAYRA, 0):
                yo_nalish = (HUJAYRA, 0)

    ilon = ilonni_harakatlantir(ilon, yo_nalish)

    # Meva yeb qo'yilsa
    if ilon[0] == meva:
        ball += 1
        tezlik = min(tezlik + 1, 15)  # Tezlikni 15 dan oshirmang
        meva = (random.randrange(0, KENGLIK, HUJAYRA), random.randrange(0, BALANDLIK, HUJAYRA))
    else:
        ilon.pop()

    if toqnashuvni_tekshir(ilon):
        game_over(ball)
        # O'yinni qayta boshlash
        ilon = [(100, 100), (80, 100), (60, 100)]
        yo_nalish = (HUJAYRA, 0)
        meva = (random.randrange(0, KENGLIK, HUJAYRA), random.randrange(0, BALANDLIK, HUJAYRA))
        ball = 0
        tezlik = 10

    ekran.fill(QORA)
    for i, qism in enumerate(ilon):
        if i == 0:
            pygame.draw.rect(ekran, YASHIL, (*qism, HUJAYRA, HUJAYRA))
            pygame.draw.circle(ekran, OQ, (qism[0] + 5, qism[1] + 6), 3)
            pygame.draw.circle(ekran, OQ, (qism[0] + HUJAYRA - 5, qism[1] + 6), 3)
            pygame.draw.circle(ekran, QORA, (qism[0] + 5, qism[1] + 6), 1)
            pygame.draw.circle(ekran, QORA, (qism[0] + HUJAYRA - 5, qism[1] + 6), 1)
        else:
            pygame.draw.rect(ekran, YASHIL, (*qism, HUJAYRA, HUJAYRA))
    pygame.draw.rect(ekran, QIZIL, (*meva, HUJAYRA, HUJAYRA))

    shrift = pygame.font.SysFont(None, 36)
    ball_matni = shrift.render(f"Ball: {ball}", True, OQ)
    ekran.blit(ball_matni, (10, 10))

    pygame.display.flip()
    soat.tick(tezlik)