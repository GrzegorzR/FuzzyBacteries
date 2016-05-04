class PopulationMutator:

    def mutate(self, population, iterations, infections =1):
        superior, inferior = self.divide_population(population)
        for i in xrange(0, iterations):




    def divide_population(self, population):
        #TODO: zaimplementowac to sortowanie
        sorted_population = sorted(population)
        return sorted_population[0:len(population)/2], sorted_population[len(population)/2:]
