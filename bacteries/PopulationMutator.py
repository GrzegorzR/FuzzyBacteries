from copy import deepcopy
from random import randint


class PopulationMutator:

    def mutate(self, population, iterations, sample, infections =1):
        superior, inferior = self.divide_population(population, sample)
        for i in xrange(0, iterations):
                self.tansfer_superior_genes(superior, inferior, sample)
        return superior + inferior



    def divide_population(self, population, sample):
        sorted_population = sorted(population, key = lambda x : x.calculate_error(sample.inputs, sample.outputs))
        return sorted_population[0:len(population)/2], sorted_population[len(population)/2:]

    def tansfer_superior_genes(self, superior, inferior, sample):
        sup_num = randint(0, len(superior) -1)
        inf_num = randint(0, len(inferior) -1)
        #inferior[inf_num] = deepcopy(superior[sup_num])
        good_gene = superior[sup_num].get_best_weighted_rule(sample)
        inferior[inf_num].change_least_weighted_rule(sample,good_gene)

