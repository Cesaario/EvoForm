from constants import *


class Goal(pygame.sprite.Sprite):
    def __init__(self, dimensao):
        super().__init__()
        self.surf = pygame.Surface(dimensao[0])
        self.surf.fill((255, 219, 18))
        self.rect = self.surf.get_rect(center=dimensao[1])
