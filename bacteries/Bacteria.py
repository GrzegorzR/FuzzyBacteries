from __future__ import division
from fuzzy.FuzzyRuleBase import FuzzyRuleBase
from random import shuffle
from copy import deepcopy
from math import ceil


class Bacteria(FuzzyRuleBase):
    def shuffle_rules(self):
        shuffle(self.fuzzy_rules)

    def calculate_iter_num(self):
        return int(ceil(len(self.fuzzy_rules) / 10.))

    def mutate_rules(self, rules_ids, mutation_degree, distribution_type="uniform"):
        for rule_id in rules_ids:
            self.fuzzy_rules[rule_id].mutate(mutation_degree, distribution_type)

    def clone(self, number_of_clones):
        return [deepcopy(self) for i in xrange(number_of_clones)]

    @staticmethod
    def transfer_chromosomes(source_bacteria, destination_bacteria, chromosome_beg_indicator, chromosomes_to_transfer):
        transfer_chromosomes_ids = slice(chromosome_beg_indicator, chromosome_beg_indicator + chromosomes_to_transfer)
        destination_bacteria.fuzzy_rules[transfer_chromosomes_ids] = \
            deepcopy(source_bacteria.fuzzy_rules[transfer_chromosomes_ids])

    @staticmethod
    def broadcast_chromosomes(source_bacteria, destination_bacterias, chromosome_beg_indicator,
                              chromosomes_to_transfer):
        for destination_bacteria_id in xrange(len(destination_bacterias)):
            Bacteria.transfer_chromosomes(source_bacteria, destination_bacterias[destination_bacteria_id],
                                          chromosome_beg_indicator, chromosomes_to_transfer)

    def improving_mutation(self, number_of_clones, input_sample):
        self.shuffle_rules()
        number_of_inputs = len(self.fuzzy_rules)
        mut_per_iter_num = self.calculate_iter_num()
        for i in xrange(0, number_of_inputs, mut_per_iter_num):
            if i + mut_per_iter_num > number_of_inputs:
                end_of_range = number_of_inputs
            else:
                end_of_range = i + mut_per_iter_num
            self.fuzzy_rules = self.improve_chromosomes(range(i, end_of_range), number_of_clones,
                                                        input_sample).fuzzy_rules

    def improve_chromosomes(self, chromosomes_to_improve, num_of_clones, input_sample):
        best_mse = self.calculate_error(input_sample.inputs, input_sample.outputs)
        best_clone_id = 0
        clones = self.clone(
                num_of_clones + 1)  # +1 zeby nie trzeba bylo sprawdzac, czy nie jest lepszy od zmutowanych klonow
        for clone_id in xrange(1, num_of_clones + 1):
            clones[clone_id].mutate_rules(chromosomes_to_improve, mutation_degree=0.7)
            cur_mse = clones[clone_id].calculate_error(input_sample.inputs, input_sample.outputs)
            if cur_mse < best_mse:
                best_clone_id = clone_id
                best_mse = cur_mse
        return clones[best_clone_id]




