import math
import random
import copy
from tqdm import tqdm


def init(n_input, n_neuron=10):
    weights = []
    weights.append([[random.gauss(0, 1) for _ in range(n_input)] for _ in range(n_neuron)])
    weights.append([[random.gauss(0, 1) for _ in range(n_neuron)] for _ in range(n_neuron)])
    weights.append([[random.gauss(0, 1) for _ in range(n_neuron)] for _ in range(4)])
    return weights

def matmul(W, x):
    return [sum([W[i][j]*x[j] for j in range(len(x))]) for i in range(len(W))]

def activation(x):
    return [1/(1+math.exp(-x_k)) for x_k in x]

def softmax(x):
    s = sum([math.exp(x_k) for x_k in x])
    return [math.exp(x_k)/s for x_k in x]

def network(weights, x):
    y_1 = activation(matmul(weights[0], x))
    y_2 = activation(matmul(weights[1], y_1))
    y_3 = softmax(matmul(weights[2], y_2))
    return y_3

def mutate(weights, factor=0.05, random_fn_1=random.random, random_fn_2=random.gauss):
    for r in weights:
        for rr in r:
            for rrr in rr:
                if random_fn_1() <= factor:
                    rrr += random_fn_2(0,1)/6
                    
def crossover(weightsA, weightsB, random_fn=random.choice):
    return [random_fn([copy.deepcopy(weightsA)[i], copy.deepcopy(weightsB)[i]]) for i in range(3)]
