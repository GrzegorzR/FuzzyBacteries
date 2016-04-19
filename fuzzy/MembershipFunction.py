from __future__ import division, print_function
from random import uniform


class MembershipFunction:
    def __init__(self, a, b, c, d, range_max, range_min, randomize=True):
        self.range_max = range_max
        self.range_min = range_min
        self.range = range_max - range_min
        if randomize:
            self.a = uniform(range_min, range_max)
            self.b = uniform(self.a, range_max)
            self.c = uniform(self.b, range_max)
            self.d = uniform(self.c, range_max)
        else:
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    def get_importance(self, x):
        if self.a <= x <= self.b:
            return (x - self.a) / (self.b - self.a)
        if self.b <= x <= self.c:
            return 1
        if self.d <= x <= self.d:
            return (self.d - x) / (self.d - self.c)

    def mutate(self, mutation_degree, distribution_type):
        mutation_range = mutation_degree * self.range
        if distribution_type == "uniform":
            self.a = uniform(max(self.a - mutation_range, self.range_min), min(self.a + mutation_range, self.range_max))
            self.b = uniform(max(self.b - mutation_range, self.range_min), min(self.b + mutation_range, self.range_max))
            self.c = uniform(max(self.c - mutation_range, self.range_min), min(self.c + mutation_range, self.range_max))
            self.d = uniform(max(self.d - mutation_range, self.range_min), min(self.d + mutation_range, self.range_max))

    def print_details(self):
        print("\t\tlower bound:", self.range_min, "upper bound:", self.range_max, "a =", self.a, "b =", self.b, "c =",
              self.c, "d =", self.d)
