from __future__ import print_function
# from fuzzy.FuzzyRule import FuzzyRule
# from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from data.function6d import get_6dsample
from bacteries.Factory import get_random_bacteria
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
    print(len(_6_d_sample.inputs[0]))
    print(len(_6_d_sample.outputs))
    print(_6_d_sample.inputs_ranges)
    print(_6_d_sample.output_range)
    bacteria = get_random_bacteria(6, _6_d_sample.inputs_ranges, _6_d_sample.output_range)
    best_mse = bacteria.calculate_error(_6_d_sample.inputs, _6_d_sample.outputs)
    print(best_mse)
    # udalo mi sie dostac blad inny niz inf po ilus tam mutacjach
    for i in xrange(10000):
        # indicator = randint(0, 5)
        bacteria.mutate_rules(0, 6, mutation_degree=1)
        cur_mse = bacteria.calculate_error(_6_d_sample.inputs, _6_d_sample.outputs)
        if cur_mse < best_mse:
            best_mse = cur_mse
        print(best_mse)
if __name__ == "__main__":
    main()
