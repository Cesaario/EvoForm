import random

import player
from constants import *
from scenario import goal


def calculate_fitness(player):
    player_pos = vec(player.rect.center)
    return player_pos.distance_to(vec(goal.rect.center))


def crossover(player_a, player_b):
    moves_length = len(player_a.ai_moves)
    crossover_indexes = random.sample(range(moves_length), int(moves_length / 2))

    a_moves = []
    b_moves = []

    for i in range(moves_length):
        if i in crossover_indexes:
            a_moves.append(player_a.ai_moves[i])
            b_moves.append(player_b.ai_moves[i])
        else:
            a_moves.append(player_b.ai_moves[i])
            b_moves.append(player_a.ai_moves[i])

    for i in range(len(a_moves)):
        if random.random() < POPULATION_SIZE:
            a_moves[i] = random.randint(1, 5)

    for i in range(len(b_moves)):
        if random.random() < POPULATION_SIZE:
            b_moves[i] = random.randint(1, 5)

    return [player.Player(True, a_moves), player.Player(True, b_moves)]


def evolve(pop):
    sorted_population = sorted(pop, key=lambda individual: individual.best_fitness)

    children = crossover(sorted_population[0], sorted_population[1])

    new_pop = [*sorted_population[:-2], *children]
    for individual in new_pop:
        individual.dead = False
        individual.ai_move = 0
        individual.time = 0

    return new_pop
