from __future__ import print_function, division
from MembershipFunction import MembershipFunction


class FuzzyRule:
    def __init__(self, number_of_inputs, input_ranges=None, output_range=None, randomize=True):
        self.number_of_inputs = number_of_inputs
        self.antecedents = [MembershipFunction(0, 0, 0, 0, boundary[1], boundary[0], randomize)
                            for boundary in input_ranges]
        self.consequence = MembershipFunction(0, 0, 0, 0, output_range[1], output_range[0], randomize)

    def mutate(self, mutation_degree, distribution_type):
        for ante_id in xrange(self.number_of_inputs):
            self.antecedents[ante_id].mutate(mutation_degree, distribution_type)
            self.consequence.mutate(mutation_degree, distribution_type)

    def get_importance(self, x):
        ante_importances = []
        for ante_id in xrange(self.number_of_inputs):
            ante_importances.append(self.antecedents[ante_id].get_importance(x))
        return min(ante_importances)

    def degranulate_nominator(self, x):
        w = self.get_importance(x)
        a, b, c, d = self.consequence.get_parameters()
        big_c = 3*w*(d**2-a**2)*(1-w)
        big_d = 3*w**2*(c*d-a*b)
        big_e = w**3*(c-d+a-b)*(c-d-a+b)
        return big_c+big_d+big_e

    def degranulate_denominator(self, x):
        w = self.get_importance(x)
        a, b, c, d = self.consequence.get_parameters()
        return 2*w*(d-a)+w**2*(c+a-d-b)

    def print_rule(self):
        print("number of inputs:", self.number_of_inputs)
        print("antecedents:")
        for i in xrange(len(self.antecedents)):
            print("\t antecedent", i)
            self.antecedents[i].print_details()
        print("\nconsequence:")
        self.consequence.print_details()
