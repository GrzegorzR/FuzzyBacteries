from __future__ import print_function
from MembershipFunction import MembershipFunction


class FuzzyRule:
    def __init__(self, number_of_inputs, number_of_outputs, input_ranges=None, output_ranges=None, randomize=True):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs
        self.antecedents = [MembershipFunction(0, 0, 0, 0, boundary[1], boundary[0], randomize)
                            for boundary in input_ranges]
        self.consequences = [MembershipFunction(0, 0, 0, 0, boundary[1], boundary[0], randomize)
                             for boundary in output_ranges]

    def mutate(self, mutation_degree, distribution_type):
        for ante_id in xrange(self.number_of_inputs):
            self.antecedents[ante_id].mutate(mutation_degree, distribution_type)
        for cons_id in xrange(self.number_of_outputs):
            self.consequences[cons_id].mutate(mutation_degree, distribution_type)

    def get_importance(self, x):
        ante_importances = []
        for ante_id in xrange(self.number_of_inputs):
            ante_importances.append(self.antecedents[ante_id].get_importance(x))
        return min(ante_importances)

    def print_rule(self):
        print("number of inputs:", self.number_of_inputs)
        print("number of outputs:", self.number_of_outputs)
        print("antecedents:")
        for i in xrange(len(self.antecedents)):
            print("\t antecedent", i)
            self.antecedents[i].print_details()
        print("\nconsequences:")
        for i in xrange(len(self.consequences)):
                print("\t consequence", i)
                self.consequences[i].print_details()
