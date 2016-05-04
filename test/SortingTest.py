
from bacteries.Factory import get_random_population
from data.function2d import get_2d_sample


def test():
    iterations = 10
    sample = get_2d_sample(2)
    population_size = 10
    population = get_random_population(20, sample.inputs_ranges, sample.output_range, population_size,
                                       sample.inputs, sample.outputs)
    for i in xrange(0, iterations):
        print("iteracja: " + str(i))
        for j in xrange(0, population_size):
            population[j].improving_mutation(5, sample)

    sorted_pop = sorted(population, key = lambda x : x.calculate_error(sample.inputs, sample.outputs))
    interior = sorted_pop[0:len(population)/2]
    superior = sorted_pop[len(population)/2:]
    for bacteria in superior:
        print bacteria.calculate_error(sample.inputs, sample.outputs)
    print "aaa"
    for bacteria in interior:
        print bacteria.calculate_error(sample.inputs, sample.outputs)


test()


