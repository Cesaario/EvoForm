from constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (0, HEIGHT - 10))