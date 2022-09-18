import random
import numpy as np
import matplotlib.pyplot as plt


def to_binary(i, n):
    b = '{0:b}'.format(i)
    while len(b) < n:
        b = '0' + b
    return b


def to_int(b):
    return int(b, 2)


assert to_int(to_binary(4, 5)) == 4


def calc_fitness(i1):
    return to_int(i1) ** 2


def choose(popu):
    fit_score = []
    cho_score = []
    cho_sequence = []
    new_popu = []
    for i in range(len(popu)):
        fit_score.append(calc_fitness(popu[i]))
        cho_score.append(random.uniform(0, 1))
    fit_score = fit_score / np.sum(fit_score)

    sorted_cho_score = sorted(cho_score)
    prob = 0
    i = 0
    for j in range(len(popu)):
        prob += fit_score[j]
        while i < len(popu) and sorted_cho_score[i] <= prob:
            cho_sequence.append(j)
            i += 1

    for i in range(len(popu)):
        new_popu.append(popu[cho_sequence[i]])

    return new_popu


def crossover(i1, i2):
    assert len(i1) == len(i2)
    n = len(i1)
    split_index = random.randint(0 + 1, n - 1)
    return '{}{}'.format(i1[:split_index], i2[split_index:]), \
           '{}{}'.format(i1[split_index:], i2[:split_index])


def mutate(i1, threshold):
    def swap_bit(c):
        if c == '0':
            return '1'
        return '0'

    return ''.join([
        swap_bit(c) if random.uniform(0, 1) <= threshold
        else c for c in i1
    ])


def ranking_population(individuals):
    return sorted(
        [(i, calc_fitness(i)) for i in individuals],
        key=lambda x: x[1], reverse=True)


n = 5
min_val = to_int('0' * n)  # '00000'
max_val = to_int('1' * n)  # '11111'

n_individuals = 4
individual_indexes = list(range(0, n_individuals))
population = [to_binary(random.randint(min_val, max_val), n)
              for i in range(0, n_individuals)]

n_matings = 1
n_iterations = 100
mutation_threshold = .01

score = []

max_val = 0
max_solution = np.zeros(len(population[0]))

for iteration in range(0, n_iterations):

    # choose
    new_population = choose(population)

    # crossovers
    for _ in range(0, n_matings):
        items_to_mate = np.random.choice(
            individual_indexes, size=2, replace=False)
        i1, i2 = crossover(
            population[items_to_mate[0]],
            population[items_to_mate[1]])
        new_population[items_to_mate[0]] = i1
        new_population[items_to_mate[1]] = i2

    for individual in new_population:
        individual = mutate(individual, mutation_threshold)

    ranked_population = ranking_population(new_population)

    if ranked_population[0][1] > max_val:
        max_val = ranked_population[0][1]
        max_solution = ranked_population[0][0]

    score.append(ranked_population[0][1])
    if iteration >= 5 and score[iteration - 5] == 961:
        break

    population = new_population

print("max：" + str(max_val))
print("x：" + str(to_int(max_solution)))

plt.plot(range(len(score)), score)
plt.xlabel("epoch")
plt.ylabel("function value")
