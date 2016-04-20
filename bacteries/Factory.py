from bacteries.Gene import Gene
from random import uniform



def get_random_gene(range_min, range_max):
    a = uniform(range_min, range_max)
    b = uniform(a, range_max)
    c = uniform(b, range_max)
    d = uniform(c, range_max)
    return Gene(a, b, c, d, range_min, range_max)

def get_random_chromosome(ranges, input):
    #TODO

