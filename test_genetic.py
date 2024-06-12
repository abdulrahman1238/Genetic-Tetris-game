import tetris_base as game
import matplotlib.pyplot as plt

chromosomes = [[2.588324907161539, 2.955249732402298, 0.6383393770374354, 0.13974804185326883, 1.6870298052389543,
                0.056522025754149]]


def evaluate_fitness(chromosome, values):
    fitness_scores = 0
    for i in range(len(chromosome)):
        fitness_scores += chromosome[i] * values[i]

    return fitness_scores


for chromosome in chromosomes:
    score = game.main(chromosome, evaluate_fitness, 600, test=True)
    if score >= 100000:
        print("you win")

best_scores = [
    1192, 1192, 1192, 1192, 1192,
    1190, 938, 1446, 1489, 1489,
    2124, 2541, 2989, 5954, 5954,
    6382, 5912, 5484, 7936, 7936,
    7936, 7007, 7007, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060
]

second_best_scores = [
    809, 1192, 1192, 1192, 1190,
    982, 938, 1237, 1446, 1404,
    1404, 1404, 2592, 2989, 5954,
    5484, 5484, 5484, 5484, 5484,
    5484, 5484, 5484, 7007, 7007,
    7007, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060,
    12060, 12060, 12060, 12060, 12060
]

states = [i + 1 for i in range(50)]

plt.plot(states, best_scores, label='Best Chromosome 1', color='blue')
plt.plot(states, second_best_scores, label='Best Chromosome 2', color='red')

plt.xlabel('States')
plt.ylabel('Score')
plt.title('Progress of Best Two Chromosomes')
plt.legend()

plt.grid(True)
plt.show()
