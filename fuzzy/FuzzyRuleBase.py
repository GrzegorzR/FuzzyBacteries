from __future__ import print_function
from random import shuffle


class FuzzyRuleBase:

    def __init__(self):
        self.fuzzy_rules = []

    def push_fuzzy_rule(self, fuzzy_rule):
        self.fuzzy_rules.append(fuzzy_rule)

    def shuffle_rules(self):
        shuffle(self.fuzzy_rules)

    def mutate_rules(self, first_rule_indicator, number_of_rules, mutation_degree, distribution_type="uniform"):
        for i in range(first_rule_indicator, first_rule_indicator + number_of_rules):
            self.fuzzy_rules[i].mutate(mutation_degree, distribution_type)

    def print_details(self):
        print("Number of rules:", len(self.fuzzy_rules))
        print("Fuzzy rules in base:")
        for i in xrange(len(self.fuzzy_rules)):
            print("\n")
            self.fuzzy_rules[i].print_rule()


    # TODO evaluating model with possible few outputs in each rule
