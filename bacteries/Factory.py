from __future__ import division
from bacteries.Gene import Gene
from bacteries.Chromosome import Chromosome
from bacteries.Bacteria import Bacteria
from random import uniform, gauss


def get_random_gene(range_min, range_max):
    a = 1
    d = 0
    while(d <a):
         a = gauss(range_min, (range_max-range_min)/3)
         d = gauss(range_max, (range_max-range_min)/3)

    b = uniform(a, d)
    c = uniform(b, d)

    return Gene(a, b, c, d, range_max, range_min)


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


def get_random_population(chromosomes_number, antecedents_ranges, consequence_range, population_size, inputs, output):
    current_size = 0
    population = []
    while current_size < population_size:
        bacteria = get_random_bacteria(chromosomes_number, antecedents_ranges, consequence_range)
        if bacteria.calculate_error(inputs, output) != float('inf'):
            population.append(bacteria)
            current_size += 1
            print("sukces")
    return population
