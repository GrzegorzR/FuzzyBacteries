from fuzzy.MembershipFunction import MembershipFunction
from random import uniform


class Gene(MembershipFunction):

     def mutate(self, mutation_degree, distribution_type):
        mutation_range = mutation_degree * (self.range_max-self.range_min)
        if distribution_type == "uniform":
            self.a = uniform(max(self.a - mutation_range, self.range_min), min(self.a + mutation_range, self.range_max))
            self.b = uniform(max(self.b - mutation_range, self.range_min), min(self.b + mutation_range, self.range_max))
            self.c = uniform(max(self.c - mutation_range, self.range_min), min(self.c + mutation_range, self.range_max))
            self.d = uniform(max(self.d - mutation_range, self.range_min), min(self.d + mutation_range, self.range_max))