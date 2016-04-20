from fuzzy.FuzzyRule import FuzzyRule


class Chromosome(FuzzyRule):

    def mutate(self, mutation_degree, distribution_type):
        for ante_id in xrange(self.number_of_inputs):
            self.antecedents[ante_id].mutate(mutation_degree, distribution_type)
            self.consequence.mutate(mutation_degree, distribution_type)