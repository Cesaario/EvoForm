import random

from pygame.locals import *

from constants import *
from scenario import platforms_array, goal


class Player(pygame.sprite.Sprite):
    on_ground = False

    def __init__(self, ai, ai_moves=None):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(100, 50))

        self.rect.bottomleft = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.ai = ai
        self.ai_moves = self.generate_moves(20)
        self.ai_move = 0
        self.time = 0
        self.dead = False

    def update(self):

        if self.dead:
            return

        pressed_keys = pygame.key.get_pressed()

        self.vel.x = 0

        if (pressed_keys[K_UP] or self.ai_movement() >= JUMP_MOVE) and self.on_ground:
            self.jump()
        if pressed_keys[K_LEFT] or self.ai_movement() == LEFT_MOVE or self.ai_movement() == LEFT_JUMP_MOVE:
            self.vel.x = -ACC
        if pressed_keys[K_RIGHT] or self.ai_movement() == RIGHT_MOVE or self.ai_movement() == RIGHT_JUMP_MOVE:
            self.vel.x = +ACC

        if not self.on_ground:
            self.vel.y += GRAV
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
        goal_collision = self.rect.collidelistall([goal])
        if goal_collision:
            print("GOAL")
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
        self.dead = True

    def ai_movement(self):
        if self.ai and self.ai_move < len(self.ai_moves):
            return self.ai_moves[self.ai_move]
        return False

    def set_time(self, time):
        self.time = time
        self.ai_move = int(self.time / MOVE_DURATION)

    def generate_moves(self, number_of_moves):
        moves = []
        for i in range(number_of_moves):
            moves.append(random.randint(1, 5))
        return moves

    def calculate_fitness(self):
        player_pos = vec(self.rect.center)
        return player_pos.distance_to(vec(goal.rect.center))

    def crossover(self, parent):
        moves_length = len(self.ai_moves)
        crossover_indexes = random.sample(range(moves_length), int(moves_length / 2))

        a_moves = []
        b_moves = []

        for i in range(moves_length):
            if i in crossover_indexes:
                a_moves.append(self.ai_moves[i])
                b_moves.append(parent.ai_moves[i])
            else:
                a_moves.append(parent.ai_moves[i])
                b_moves.append(self.ai_moves[i])

        print(self.ai_moves, parent.ai_moves)
        print(a_moves, b_moves)

        return [Player(True, a_moves), Player(True, b_moves)]
