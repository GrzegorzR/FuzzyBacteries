from bacteries.Gene import Gene
from bacteries.Chromosome import Chromosome
from bacteries.Bacteria import Bacteria
from random import uniform


def get_random_gene(range_min, range_max):
    a = uniform(range_min, range_max)
    b = uniform(a, range_max)
    c = uniform(b, range_max)
    d = uniform(c, range_max)
    return Gene(a, b, c, d, range_min, range_max)


def get_random_chromosome(antecedents_ranges, consequence_range):
    antecedents = []
    consequence = get_random_gene(consequence_range[0], consequence_range[1])
    for rang in antecedents_ranges:
        antecedents.append(get_random_gene(rang[0], rang[1]))
    return Chromosome(antecedents, consequence)


def get_random_bacteria(chromosomes_number, antecedents_ranges, consequence_range):
    result = Bacteria()
    for i in range(0, chromosomes_number):
        result.push_fuzzy_rule(get_random_chromosome(antecedents_ranges, consequence_range))
    return result
