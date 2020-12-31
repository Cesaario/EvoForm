from pygame.locals import *
from constants import *
from scenario import platforms, platforms_array


class Player(pygame.sprite.Sprite):
    on_ground = False

    def __init__(self, ai):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(100, 50))

        self.rect.bottomleft = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.ai = ai

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        self.vel.x = 0

        if pressed_keys[K_UP] and self.on_ground:
            self.jump()
        if pressed_keys[K_LEFT]:
            self.vel.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.vel.x = +ACC

        if not self.on_ground:
            self.vel.y += GRAV
            print(self.vel.y)
            if self.vel.y > MAX_GRAV:
                self.vel.y = MAX_GRAV

        self.rect.left += self.vel.x
        self.handle_collision(HORIZONTAL)

        self.rect.top += self.vel.y
        self.on_ground = False
        self.handle_collision(VERTICAL)

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT:
            self.death()

    def handle_collision(self, direction):
        for platform in [platforms_array[i] for i in self.rect.collidelistall(platforms_array)]:
            if direction == HORIZONTAL:
                if self.vel.x > 0:
                    self.rect.right = platform.rect.left
                if self.vel.x < 0:
                    self.rect.left = platform.rect.right
            if direction == VERTICAL:
                if self.vel.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.vel.y = 0
                if self.vel.y < 0:
                    self.rect.top = platform.rect.bottom

    def jump(self):
        self.vel.y -= JUMP

    def death(self):
        self.rect.bottomleft = vec((10, 385))
