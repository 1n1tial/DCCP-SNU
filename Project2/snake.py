import os
import time
import random
import math
from typing import Callable
from dataclasses import field, dataclass

@dataclass
class SnakeGame:
    # random.seed(random.choice([0, 1, 2]))
    n_size: int = 10
    directions: list = field(default_factory=list)

    snake: list = field(default_factory=list)
    fruit: tuple = (random.randint(0, n_size - 1), random.randint(0, n_size - 1))

    current_dir: list = field(default_factory=list)
    score: int = 0
    lifetime: int = 0
    fitness: int = 0

    clear: Callable = lambda: os.system('cls') # windows에서는 이것을 쓰세요
    # self.clear = lambda: os.system('clear') # linux, mac에서는 이것을 쓰세요

    def __post_init__(self) -> None:
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.snake = [[self.n_size // 2, self.n_size // 2]]
        self.snake.append([self.snake[0][0] - 1, self.snake[0][1]])
        self.current_dir = [1, 0]
        while (self.fruit[0] == self.n_size // 2 and self.fruit[1] == self.n_size // 2) or (self.fruit[0] == self.n_size // 2 - 1 and self.fruit[1] == self.n_size // 2):
            self.fruit = (random.randint(0, self.n_size - 1), random.randint(0, self.n_size - 1))

def move(self, dir, random_fn=random.randint):
    dir_dict = {0: [-1, 0], 1: [1, 0], 2: [0, -1], 3: [0, 1]}
    # - ignore if the direction is opposite to the current direction
    if not self.directions[dir] == self.current_dir:
        self.current_dir = dir_dict[dir]
    # - wall collision
    if self.snake[0][0] + self.current_dir[0] < 0 or self.snake[0][0] + self.current_dir[0] >= self.n_size:
        return False
    if self.snake[0][1] + self.current_dir[1] < 0 or self.snake[0][1] + self.current_dir[1] >= self.n_size:
        return False
    # - body collision
    for i in range(3, len(self.snake)-1): # the head can only collide with the third body part and following, and cannot collide with the last body part(since the last body part will move)
        if [self.snake[0][0] + self.current_dir[0], self.snake[0][1] + self.current_dir[1]] == self.snake[i]:
            return False
    # since the snake moved on, increment lifetime
    self.lifetime += 1
    # - move snake
    # first, simply insert new head
    self.snake.insert(0, [self.snake[0][0] + self.current_dir[0], self.snake[0][1] + self.current_dir[1]])
    # if there was no fruit, remove the last body part
    if (self.snake[0][0], self.snake[0][1]) != self.fruit:
        self.snake.pop()
    # - if there was fruit, do not remove last part and reposition fruit
    else:
        # - form a set of tuples of all possible coordinates and subtract the set containing the coordinates of the current snake body parts
        available_spots = list(set(((j, k) for j in range(self.n_size) for k in range(self.n_size))) - set(tuple(part) for part in self.snake))
        self.fruit = available_spots[random_fn(0, len(available_spots)-1)]
    # - raising scores
        self.score += 1
    return True

def get_input(self):
    wall_input = [0 for _ in range(4)]
    body_input = [0 for _ in range(4)]
    fruit_input = [0 for _ in range(4)]

    # - inverse distance from wall
    wall_input = [1/(self.n_size - self.snake[0][0]), 1/(self.snake[0][0] + 1), 1/(self.n_size - self.snake[0][1]), 1/(self.snake[0][1] + 1)]
    # - inverse distance from body
    for i, dir in enumerate(self.directions):
        for j in range(1, self.n_size):
            if [self.snake[0][0] + j * dir[0], self.snake[0][1] + j * dir[1]] in self.snake:
                body_input[i] = 1/j
                break
    # - position of fruit
    if self.snake[0][0] < self.fruit[0]: fruit_input[0] = 10
    elif self.snake[0][0] > self.fruit[0]: fruit_input[1] = 10
    if self.snake[0][1] < self.fruit[1]: fruit_input[2] = 10
    elif self.snake[0][1] > self.fruit[1]: fruit_input[3] = 10
    
    return wall_input + body_input + fruit_input
    
def calculate_fitness(snake):
    # snake: SnakeGame 클래스의 변수
    fitness = snake.lifetime + 100 * snake.score
    snake.fitness = fitness
    return fitness
    
    
def print_game(self, title="Snake"):
    # self.clear()
    print(title)
    print("O", end='')
    for _ in range(self.n_size):
        print("- ", end='')
    print("O")

    for row in range(self.n_size):
        print("|", end="")
        for col in range(self.n_size):
            printed = False
            for body in self.snake:
                if col == body[0] and row == body[1]:
                    print("O ", end='')
                    printed = True
            if not printed and col == self.fruit[0] and row == self.fruit[1]:
                print("A ", end='')
                printed = True
            if not printed:
                print("  ", end='')
        print("|")
    print("O", end='')
    for _ in range(self.n_size):
        print("- ", end='')
    print("O")
    print(f"SCORE: {self.score}")
    # time.sleep(0.5)

if __name__ == '__main__':
    snake = SnakeGame()
    print_game(snake)
    move(snake, 0)
    print_game(snake)
    get_input(snake)