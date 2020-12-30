import pygame
from platform import Platform
from constants import *

def gerar_dimensao(x, y, largura):
    return [(largura, ALTURA_PLAT), (x + largura/2, HEIGHT - y - ALTURA_PLAT/2)]

platforms_array = []

platforms_array.append(Platform(gerar_dimensao(0, 0, 200)))
platforms_array.append(Platform(gerar_dimensao(275, 100, 100)))
platforms_array.append(Platform(gerar_dimensao(50, 200, 100)))
platforms_array.append(Platform(gerar_dimensao(200, 325, 400)))
platforms_array.append(Platform(gerar_dimensao(700, 400, 100)))

platforms = pygame.sprite.Group()
for platform in platforms_array:
    platforms.add(platform)