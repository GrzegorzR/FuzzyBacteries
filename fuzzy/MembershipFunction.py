from __future__ import division, print_function
from random import uniform


class MembershipFunction:

    def __init__(self, a, b, c, d, range_max, range_min):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.range_max = range_max
        self.range_min = range_min

    def get_importance(self, x):
        if self.a <= x <= self.b:
            return (x - self.a) / (self.b - self.a)
        if self.b <= x <= self.c:
            return 1
        if self.d <= x <= self.d:
            return (self.d - x) / (self.d - self.c)
        return 0

    def get_parameters(self):
        return self.a, self.b, self.c, self.d

    def print_details(self):
        print("\t\tlower bound:", self.range_min, "upper bound:", self.range_max, "a =", self.a, "b =", self.b, "c =",
              self.c, "d =", self.d)
