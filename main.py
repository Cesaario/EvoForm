import sys

from pygame.locals import *

from constants import *
from player import Player
from scenario import platforms_array, goal

status = pygame.init()
if status[1] > 0:
    print("Erro!")
    sys.exit(-1)
else:
    print("Sucesso!")

FramesPerSecond = pygame.time.Clock()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EvoForm")

players = []
for i in range(10):
    ai_player = Player(True)
    players.append(ai_player)

all_sprites = pygame.sprite.Group()
for platform in platforms_array:
    all_sprites.add(platform)
all_sprites.add(goal)

for ai_player in players:
    all_sprites.add(ai_player)

frames = 0
seconds = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((51, 51, 51))

    for entity in all_sprites:
        if isinstance(entity, Player) and entity.dead:
            continue
        display_surface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramesPerSecond.tick(FPS)

    frames += 1
    seconds = frames / FPS

    for ai_player in players:
        ai_player.set_time(seconds)
        ai_player.update()
