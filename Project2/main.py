from snake import SnakeGame, move, get_input, calculate_fitness, print_game
from network import init, network, mutate, crossover

from itertools import combinations
from tqdm import tqdm
import random
import copy
import time
import pickle

# random.seed(0)

def main():
    n_generations = 100
    n_population = 1000
    n_parents = 10

    over_1000 = False
    while not over_1000:
        population = [init(12) for _ in range(n_population)]
        max_fitness = 0
        winner = None
        pbar = tqdm(range(n_generations))
        for epoch in pbar:
            # simulate
            fitnesses = []
            for weights in population:
                snake = SnakeGame()
                code = True
                step = 0
                while code and step < 300:
                    x = get_input(snake)
                    step += 1
                    pred = network(weights, x)
                    max_index = 0
                    for j in range(4):
                        if pred[j] == max(pred):
                            max_index = j
                            break
                    code = move(snake, max_index)
                fitness = calculate_fitness(snake)
                fitnesses.append(fitness)

            pbar.set_postfix(fitness=max(fitnesses))
            if max_fitness <= max(fitnesses):
                max_index = 0
                for j in range(n_population):
                    if fitnesses[j] == max(fitnesses):
                        max_index = j
                        break
                max_fitness = max(fitnesses)
                winner = copy.copy(population[max_index])
            
            # evolve
            if epoch < n_generations - 1:
                new_population = []
                sorted_index = sorted(range(len(fitnesses)), key=lambda x:fitnesses[x])
                parents = [population[v] for v in sorted_index[-n_parents:]]
                pairs = list(combinations(parents, 2))
                n_children = n_population // len(pairs)
                for weightsA, weightsB in pairs:
                    for _ in range(n_children):
                        child = crossover(weightsA, weightsB)
                        mutate(child)
                        new_population.append(child)
                population = new_population

                if epoch > 20:
                    if max_fitness >= 1000:
                        over_1000 = True
                    else:
                        break

    # simulate
    code = True
    snake = SnakeGame()
    print(winner)
    while code:
        print_game(snake)
        x = get_input(snake)
        print(f"wall: {x[:4]}")
        print(f"body: {x[4:8]}")
        print(f"fruit: {x[8:]}")
        pred = network(winner, x)
        max_index = 0
        for j in range(4):
            if pred[j] == max(pred):
                max_index = j
                break
        code = move(snake, max_index)
        time.sleep(0.5)
    score = calculate_fitness(snake)
    print(score)
    if score >= 300:
        with open('winner.pkl', 'wb') as f:
            pickle.dump(winner, f)


if __name__ == '__main__':
    main()