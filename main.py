from __future__ import print_function
from fuzzy.FuzzyRule import FuzzyRule
from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from data.function6d import get_6dsample


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
    print(get_6dsample(10000), get_6dsample(10000))


if __name__ == "__main__":
    main()
