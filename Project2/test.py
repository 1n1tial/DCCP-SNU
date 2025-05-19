from snake import SnakeGame, move, get_input, calculate_fitness, print_game
from network import init, network, mutate, crossover

import time
import pickle

def main():
    with open(file='winner.pkl', mode='rb') as f:
        winner = pickle.load(f)

    # simulate
    code = 1
    snake = SnakeGame()
    print(winner)
    while code == 1:
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


if __name__ == '__main__':
    main()