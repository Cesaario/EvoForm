import sys
from constants import *
from player import Player
from scenario import Platform1
from pygame.locals import *

status = pygame.init()
if status[1] > 0:
    print("Erro!")
    sys.exit(-1)
else:
    print("Sucesso!")

FramesPerSecond = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EvoForm")

Player1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(Platform1)
all_sprites.add(Player1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((51, 51, 51))

    for entity in all_sprites:
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramesPerSecond.tick(FPS)

    Player1.move()
    Player1.update()