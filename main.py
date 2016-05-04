from __future__ import print_function
import matplotlib.pyplot as plt
from matplotlib import cm
from data.function6d import get_6dsample
from data.function2d import get_2d_sample
from bacteries.Factory import get_random_population
from bacteries.Bacteria import Bacteria
from bacteries.PopulationMutator import PopulationMutator

from copy import deepcopy
from scipy.optimize import root
from numpy import arange
from math import sin, cos
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from random import uniform


# from random import randint

def fun(x, y, bacteria):
    if (x == 0):
        print(y)
    return bacteria.evaluate((x, y))


def fun2(x, y):
    return sin(x) + cos(y)


def plotResult(bacteria):
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    x = y = np.arange(0, 6.0, 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array([fun(x, y, bacteria) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z)

    ax = ax = fig.add_subplot(1, 2, 2, projection='3d')
    zs = np.array([fun2(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)
    ax.plot_surface(X, Y, Z)
    plt.show()


def main():
    population_mutator = PopulationMutator()
    iterations = 100
    sample = get_2d_sample(10)
    population_size = 10
    population = get_random_population(10, sample.inputs_ranges, sample.output_range, population_size,
                                       sample.inputs, sample.outputs)
    for i in xrange(0, iterations):
        print("iteracja: " + str(i))
        for j in xrange(0, population_size):
            population[j].improving_mutation(5, sample)
            print(population[j].calculate_error(sample.inputs, sample.outputs))

        # ten population mutator nie dziala, nie wiem czemu 
        population_mutator.mutate(population, 10, sample)
        print ("po transferze genow")
        for j in xrange(0, population_size):
            print(population[j].calculate_error(sample.inputs, sample.outputs))

    best = None
    best_val = 1000
    for bacteria in population:
        if bacteria.calculate_error(sample.inputs, sample.outputs) < best_val:
            best = bacteria

    plotResult(best)


if __name__ == "__main__":
    main()
