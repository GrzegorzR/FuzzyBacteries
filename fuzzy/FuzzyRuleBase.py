from __future__ import print_function, division
from random import shuffle


class FuzzyRuleBase:

    def __init__(self):
        self.fuzzy_rules = []

    def push_fuzzy_rule(self, fuzzy_rule):
        self.fuzzy_rules.append(fuzzy_rule)

    def shuffle_rules(self):
        shuffle(self.fuzzy_rules)

    def mutate_rules(self, first_rule_indicator, number_of_rules, mutation_degree, distribution_type="uniform"):
        for rule_id in range(first_rule_indicator, first_rule_indicator + number_of_rules):
            self.fuzzy_rules[rule_id].mutate(mutation_degree, distribution_type)

    def print_details(self):
        print("Number of rules:", len(self.fuzzy_rules))
        print("Fuzzy rules in base:")
        for rule_id in xrange(len(self.fuzzy_rules)):
            print("\n")
            self.fuzzy_rules[rule_id].print_rule()

    def evaluate(self, input_vector):
        nominator = 0
        denominator = 0
        for rule_id in xrange(len(self.fuzzy_rules)):
            nominator += self.fuzzy_rules[rule_id].degranulate_nominator(input_vector[rule_id])
            denominator += self.fuzzy_rules[rule_id].degranulate_denominator(input_vector[rule_id])
        if denominator != 0:
            return nominator/(3*denominator)
        return float('inf')
