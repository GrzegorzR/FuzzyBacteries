from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from random import shuffle


class Bacteria(FuzzyRuleBase):

    def shuffle_rules(self):
        shuffle(self.fuzzy_rules)

    def mutate_rules(self, first_rule_indicator, number_of_rules, mutation_degree, distribution_type="uniform"):
        for rule_id in range(first_rule_indicator, first_rule_indicator + number_of_rules):
            self.fuzzy_rules[rule_id].mutate(mutation_degree, distribution_type)
