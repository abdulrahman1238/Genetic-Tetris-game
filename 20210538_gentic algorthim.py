import random
import string

TARGET = 'cognitive science'
GENES = string.ascii_letters + ' '

POP_SIZE = 500
MUT_RATE = 0.1
MAX_GENERATIONS = 1e9


def init_pop():
    return ''.join(random.choices(GENES, k=len(TARGET)))


def fitness(chromosome):
    return sum(1 for expected, actual in zip(TARGET, chromosome) if expected != actual)


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(chromosome):
    mutated_chromosome = list(chromosome)
    for i in range(len(mutated_chromosome)):
        if random.random() < MUT_RATE:
            mutated_chromosome[i] = random.choice(GENES)
    return ''.join(mutated_chromosome)


def main():
    population = [init_pop() for _ in range(POP_SIZE)]
    generation = 0

    while generation < MAX_GENERATIONS:
        population.sort(key=lambda chromosome: fitness(chromosome))
        best_chromosome = population[0]
        best_fitness = fitness(best_chromosome)

        if best_fitness == 0:
            print(f"Target string '{TARGET}' generated in {generation} generations: {best_chromosome}")
            break

        selected_parents = population[:int(POP_SIZE / 2)]
        new_generation = []

        while len(new_generation) < POP_SIZE:
            parent1, parent2 = random.choices(selected_parents, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_generation.extend([child1, child2])

        population = new_generation
        generation += 1

    if generation == MAX_GENERATIONS:
        print(f"Target string '{TARGET}' not generated in {MAX_GENERATIONS} generations.")



main()







