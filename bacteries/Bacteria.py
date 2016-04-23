from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from random import shuffle
from copy import deepcopy


class Bacteria(FuzzyRuleBase):

    def shuffle_rules(self):
        shuffle(self.fuzzy_rules)

    def mutate_rules(self, first_rule_indicator, number_of_rules, mutation_degree, distribution_type="uniform"):
        for rule_id in xrange(first_rule_indicator, first_rule_indicator + number_of_rules):
            self.fuzzy_rules[rule_id].mutate(mutation_degree, distribution_type)

    def clone(self, number_of_clones):
        return [deepcopy(self) for i in xrange(number_of_clones)]

    @staticmethod
    def transfer_chromosomes(source_bacteria, destination_bacteria, chromosome_beg_indicator, chromosomes_to_transfer):
        transfer_chromosomes_ids = slice(chromosome_beg_indicator, chromosome_beg_indicator+chromosomes_to_transfer)
        destination_bacteria.fuzzy_rules[transfer_chromosomes_ids] = \
            deepcopy(source_bacteria.fuzzy_rules[transfer_chromosomes_ids])

    @staticmethod
    def broadcast_chromosomes(source_bacteria, destination_bacterias, chromosome_beg_indicator, chromosomes_to_transfer):
        for destination_bacteria_id in xrange(len(destination_bacterias)):
            Bacteria.transfer_chromosomes(source_bacteria, destination_bacterias[destination_bacteria_id],
                                          chromosome_beg_indicator, chromosomes_to_transfer)

