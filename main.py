from __future__ import print_function
# from fuzzy.FuzzyRule import FuzzyRule
# from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from data.function6d import get_6dsample
from bacteries.Factory import get_random_population
from bacteries.Bacteria import Bacteria
from copy import deepcopy
from scipy.optimize import root
# from random import randint


def main():
    """
    input_ranges = [[0, 5], [-2, 6], [-5.4, -1.2]]
    in_len = len(input_ranges)
    output_range = [-3.3, 3.3]

    test_rule_0_filled = FuzzyRule(in_len, input_ranges=input_ranges, output_range=output_range,
                                   randomize=False)
    test_rule_uni_rand_filled = FuzzyRule(in_len, input_ranges=input_ranges, output_range=output_range)

    print("Rule filled with zeros")
    test_rule_0_filled.print_rule()

    print("\n\nRule filled randomly")
    test_rule_uni_rand_filled.print_rule()
    test_fuzzy_rule_base = FuzzyRuleBase()
    test_fuzzy_rule_base.shuffle_rules()
    test_fuzzy_rule_base.push_fuzzy_rule(test_rule_0_filled)
    test_fuzzy_rule_base.push_fuzzy_rule(test_rule_uni_rand_filled)
    test_fuzzy_rule_base.mutate_rules(0, 2, 0.5)

    print("\n\nMutated fuzzy rule base")
    test_fuzzy_rule_base.print_details()

    print("\n\nGet truncated importance of first rule in 1")
    print(test_fuzzy_rule_base.fuzzy_rules[0].get_importance(1))

    input_vector = [2, -1, -1.5]
    print("\n\nEvaluate model for input vector :", input_vector)
    print(test_fuzzy_rule_base.evaluate(input_vector))
    """
    _6_d_sample = get_6dsample(100)
    max_generation_number = 2
    population_size = 5
    population = get_random_population(6, _6_d_sample.inputs_ranges, _6_d_sample.output_range, population_size, _6_d_sample.inputs, _6_d_sample.outputs)
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
                    clones[clone_id].mutate_rules(rule_indicator, number_of_rules_mut_per_itteration, mutation_degree=0.7)
                    cur_mse = clones[clone_id].calculate_error(_6_d_sample.inputs, _6_d_sample.outputs)
                    if cur_mse < best_mse:
                        best_clone_id = clone_id
                        best_mse = cur_mse
                Bacteria.broadcast_chromosomes(clones[best_clone_id], clones, rule_indicator, number_of_rules_mut_per_itteration)
            population[bacteria_id] = deepcopy(clones[best_clone_id])
            #TODO Zbudowanie tutaj tego masakrytycznego rozwiazania LM

    for bacteria in population:
        print(bacteria.calculate_error(_6_d_sample.inputs, _6_d_sample.outputs))

if __name__ == "__main__":
    main()