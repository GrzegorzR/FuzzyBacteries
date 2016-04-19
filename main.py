from fuzzy.FuzzyRule import FuzzyRule
from fuzzy.FuzzyRuleBase import FuzzyRuleBase

def main():
    input_ranges = [[0, 5], [-2, 6], [-5.4, -1.2]]
    in_len = len(input_ranges)
    output_ranges = [[-3.3, 3.3]]
    out_len = len(output_ranges)

    test_rule_0_filled = FuzzyRule(in_len, out_len, input_ranges=input_ranges, output_ranges=output_ranges,
                                   randomize=False)
    test_rule_uni_rand_filled = FuzzyRule(in_len, out_len, input_ranges=input_ranges, output_ranges=output_ranges)

    print("Rule filled with zeros")
    test_rule_0_filled.print_rule()

    print("\n\nRule filled randomly")
    test_rule_uni_rand_filled.print_rule()
    test_fuzzy_rule_base = FuzzyRuleBase()
    test_fuzzy_rule_base.shuffle_rules()
    test_fuzzy_rule_base.push_fuzzy_rule(test_rule_0_filled)
    test_fuzzy_rule_base.push_fuzzy_rule(test_rule_uni_rand_filled)
    test_fuzzy_rule_base.mutate_rules(0, 2, 0.5)

    print("\n\nMutated filled with zeros rule")
    test_fuzzy_rule_base.fuzzy_rules[0].print_rule()

    test_rule_0_filled.get_importance(1)

if __name__ == "__main__":
    main()
