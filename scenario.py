from constants import *
from goal import Goal
from platform import Platform


def gerar_dimensao(x, y, largura, altura=None):
    if not altura:
        altura = ALTURA_PLAT
    return [(largura, altura), (x + largura / 2, HEIGHT - y - altura / 2)]


platforms_array = []

platforms_array.append(Platform(gerar_dimensao(0, 0, 200)))
platforms_array.append(Platform(gerar_dimensao(275, 100, 100)))
platforms_array.append(Platform(gerar_dimensao(50, 200, 100)))
platforms_array.append(Platform(gerar_dimensao(200, 325, 400)))
platforms_array.append(Platform(gerar_dimensao(700, 400, 100)))

goal = Goal(gerar_dimensao(730, 420, 50, 50))

platforms = pygame.sprite.Group()
for platform in platforms_array:
    platforms.add(platform)
