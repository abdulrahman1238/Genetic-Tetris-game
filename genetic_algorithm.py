import tetris_base as game
import random
import copy
import matplotlib.pyplot as plt
random.seed(7)


population_size = 20
chromosome_size = 6
generation_size = 50
crossover_rate = 0.25
mutation_rate = 0.1
#heuristic_initialization = [[1.6464990227079859, 2.955249732402298, 0.6383393770374354, 0.13974804185326883, 1.6124289550227213, 0.056522025754149],[2.6547986377908463, 2.955249732402298, 1.1448798198377466, 0.13974804185326883, 1.32037473715483, 0.056522025754149],[1.9413865635830063, 2.955249732402298, 0.6383393770374354, 0.13974804185326883, 1.6870298052389543, 0.056522025754149]]
heuristic_initialization = []

# this for play not genetic
num_iteration = 500


def initialize_population(population_size, chromosome_size,heuristic_initialization):
    population = []
    for _ in range(population_size - len(heuristic_initialization)):
        chromosome = [random.uniform(0, 3.0) for _ in range(chromosome_size)]
        population.append(chromosome)
    for chromosome in heuristic_initialization:
        population.append(chromosome)
    return population


def evaluate_fitness(chromosome, values):
    fitness_scores = 0
    for i in range(len(chromosome)):
        fitness_scores += chromosome[i] * values[i]

    return fitness_scores


def selection(population, fitness_scores):
    selected_population = []

    total_fitness = sum(fitness_scores)
    fitness_probabilities = [fitness / total_fitness for fitness in fitness_scores]

    cumulative_probabilities = [sum(fitness_probabilities[:i + 1]) for i in range(len(fitness_probabilities))]

    for _ in range(len(population)):
        spin = random.random()

        for i, cumulative_prob in enumerate(cumulative_probabilities):
            if spin < cumulative_prob:
                selected_population.append(population[i])
                break

    return selected_population


def crossover(population, crossover_rate):
    selected_population = []
    index_selected = []

    for j, chromosome in enumerate(population):
        random_rate = random.random()
        #print(random_rate)
        if random_rate < crossover_rate:
            selected_population.append(chromosome)
            index_selected.append(j)

    children = []
    #print(selected_population)
    num_chromosomes = len(selected_population)

    for i in range(0, num_chromosomes):
        parent1 = selected_population[i]
        parent2 = selected_population[(i + 1) % num_chromosomes]

        crossover_point = random.randint(1, len(parent1) - 1)

        child = parent1[:crossover_point] + parent2[crossover_point:]

        children.append(child)
    #print(f'children = {children}')
    return children, index_selected


def update_population_after_crossover(population, offspring_population, index_selected):
    for i in range(len(index_selected)):
        j = index_selected[i]
        population[j] = offspring_population[i]

    return population


def mutation(population, mutation_rate):
    mutated_population = []

    for chromosome in population:
        mutated_chromosome = []
        for gene in chromosome:
            if random.random() < mutation_rate:
                mutated_gene = random.uniform(0.0, 3.0)
            else:
                mutated_gene = gene

            mutated_chromosome.append(mutated_gene)

        mutated_population.append(mutated_chromosome)

    return mutated_population


def genetic_algorithm(population_size, chromosome_size, generation_size, crossover_rate, mutation_rate):
    all_fitness_scores = []
    all_population = []
    best_population = []
    second_best_population = []
    # Initialize population
    population = initialize_population(population_size, chromosome_size,heuristic_initialization)

    for generation in range(generation_size):
        # Evaluate fitness
        fitness_scores = []
        i = 1

        for chromosome in population:
            score = game.main(chromosome, evaluate_fitness, num_iteration, generation, i)
            fitness_scores.append(score)
            i += 1

        all_population.append(population)
        all_fitness_scores.append(fitness_scores)
        print(population)
        print('\n')
        print(fitness_scores)
        print('\n\n')

        fitness_scores_sorted, population_sorted = zip(*sorted(zip(copy.deepcopy(fitness_scores), copy.deepcopy(population)), key=lambda x: x[0]))
        best_population.append([population_sorted[-1], fitness_scores_sorted[-1]])
        second_best_population.append([population_sorted[-2], fitness_scores_sorted[-2]])
        # Selection
        population = selection(population, fitness_scores)

        # Crossover
        offspring_population, index_selected = crossover(population, crossover_rate)

        # update population after crossover
        population = update_population_after_crossover(population, offspring_population, index_selected)

        # Mutation
        population = mutation(population, mutation_rate)

    return all_population, all_fitness_scores, best_population, second_best_population


all_population, all_fitness_scores, best_population, second_best_population = genetic_algorithm(population_size, chromosome_size, generation_size, crossover_rate, mutation_rate)
print(best_population)
print(second_best_population)
best_sorted = sorted(best_population, key=lambda x: x[1])
second_best_sorted = sorted(second_best_population, key=lambda x: x[1])
best_chromosome = best_sorted[-1]
second_best_chromosome = max(second_best_sorted[-1], best_sorted[-2])

print(f'\n\n\n best chromosome = {best_chromosome}\n')
print(f'\n\n\n second best chromosome = {second_best_chromosome}\n')


print(initialize_population(population_size, chromosome_size, heuristic_initialization))


def log_values_to_file(all_population, all_fitness_scores, best_population, second_best_population, best_chromosome, second_best_chromosome, filename):
    with open(filename, 'w') as f:
        f.write(f"  \t\t\t\tchromosome\t\tscore\n")
        generation = 1
        for value1, value2 in zip(all_population, all_fitness_scores):
            index = 1
            for x, y in zip(value1, value2):
                f.write(f"{index}-\tgeneration = {generation}\t{x}\t\t{y}\n\n")
                index += 1
            generation += 1
            f.write('\n\n')

        f.write(f"\nbest chromosome in each generation\t\tscore:\n")
        f.write(best_population)
        i = 1
        for x in best_population:
            f.write(f"generation{i},\t{x[0]}\t{x[1]}\n")
            i += 1
        f.write(f"\nsecond best chromosome in each generation\t\tscore:\n")
        f.write(second_best_population)
        i = 1
        for x in second_best_population:
            f.write(f"generation{i},\t{x[0]}\t{x[1]}\n")
            i += 1
        f.write(f"\nthe best chromosome in all generations = {best_chromosome[0]}\t\tscore: = {best_chromosome[1]}\n")
        f.write(f"\nthe second best chromosome in all generations = {second_best_chromosome[0]}\t\tscore: = {second_best_chromosome[1]}\n")
        f.write(f"\nall population = {all_population}\n")
        f.write(f"\nall score = {all_fitness_scores}\n")



log_values_to_file(all_population, all_fitness_scores, best_population, second_best_population, best_chromosome, second_best_chromosome, 'training_gentic_final')

# chromosomes = [[2.561821550437845, 2.9006691946675884, 2.3385869192878674, 0.09322776437310831, 2.40136385293821, 0.12589772769744]]

states = [i for i in range(600)]
best_population_score = [i[1] for i in best_population]
second_best_population_score = [i[1] for i in second_best_population]

plt.plot(states, best_population, label='Best Chromosome 1', color='blue')
plt.plot(states, second_best_population, label='Best Chromosome 2', color='red')

plt.xlabel('States')
plt.ylabel('Score')
plt.title('Progress of Best Two Chromosomes')
plt.legend()

plt.grid(True)
plt.show()




