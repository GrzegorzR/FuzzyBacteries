from __future__ import print_function
import matplotlib as plt
# from fuzzy.FuzzyRule import FuzzyRule
# from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from data.function6d import get_6dsample
from data.function2d import get_2d_sample
from bacteries.Factory import get_random_population
from bacteries.Bacteria import Bacteria
from copy import deepcopy
from scipy.optimize import root
from numpy import arange

# from random import randint


def costam():
    _6_d_sample = get_6dsample(100)
    max_generation_number = 2
    population_size = 5
    population = get_random_population(6, _6_d_sample.inputs_ranges, _6_d_sample.output_range, population_size,
                                       _6_d_sample.inputs, _6_d_sample.outputs)
    """
    number_of_clones = 5
    number_of_inputs = population[0].fuzzy_rules[0].number_of_inputs
    number_of_rules_mut_per_itteration = 6
    for generation_number in xrange(max_generation_number):
        for bacteria_id in xrange(population_size):
            population[bacteria_id].shuffle_rules()
            best_mse = population[bacteria_id].calculate_error(_6_d_sample.inputs, _6_d_sample.outputs)
            clones = population[bacteria_id].clone(number_of_clones)
            for rule_indicator in xrange(0, number_of_inputs, number_of_rules_mut_per_itteration):
                best_clone_id = -1
                for clone_id in xrange(number_of_clones):
                    clones[clone_id].mutate_rules(rule_indicator, number_of_rules_mut_per_itteration,
                                                  mutation_degree=0.7)
                    cur_mse = clones[clone_id].calculate_error(_6_d_sample.inputs, _6_d_sample.outputs)
                    if cur_mse < best_mse:
                        best_clone_id = clone_id
                        best_mse = cur_mse
                Bacteria.broadcast_chromosomes(clones[best_clone_id], clones, rule_indicator,
                                               number_of_rules_mut_per_itteration)
            population[bacteria_id] = deepcopy(clones[best_clone_id])
            # TODO Zbudowanie tutaj tego masakrytycznego rozwiazania LM

    for bacteria in population:
        print(bacteria.calculate_error(_6_d_sample.inputs, _6_d_sample.outputs))
    """

def plotResult(bacteria):
    xs = []
    ys = []
    out = []
    for x in arange(0,6,0.5):
        for y in arange(0,6,0.5):
            xs.append(x)
            ys.append(ys)
            out.append(bacteria.evaluate((x,y)))
    plt.plot(xs,ys,out)
def main():
    iterations = 10
    sample = get_2d_sample(5)
    population_size = 1
    population = get_random_population(100, sample.inputs_ranges, sample.output_range, population_size,
                                       sample.inputs, sample.outputs)
    for i in xrange(0,iterations):
        print ("iteracja: " + str(i))
        for j in xrange(0,population_size):
            population[j].improving_mutation(5,sample)
            print (population[j].calculate_error(sample.inputs, sample.outputs))

    best = None
    best_val = 1000
    for bacteria in population:
        if bacteria.calculate_error(sample.inputs, sample.outputs) < best_val:
            best = bacteria

    plotResult(best)


if __name__ == "__main__":
        main()
