from __future__ import print_function, division



class FuzzyRuleBase:

    def __init__(self):
        self.fuzzy_rules = []

    def push_fuzzy_rule(self, fuzzy_rule):
        self.fuzzy_rules.append(fuzzy_rule)



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


    def calculate_error(self, inputs, results):
        computated = []
        #TODO na numpy byloby latwiej hcyba
        for input in inputs:
            computated.append(self.evaluate(input))
        #podobno mean square error, ale chuj wie
        return((results - computated) ** 2).mean(axis = None)