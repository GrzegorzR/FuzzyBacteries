from __future__ import print_function, division

from copy import deepcopy

import numpy as np
# from math import sqrt

class FuzzyRuleBase:

    def __init__(self):
        self.fuzzy_rules = []

    def push_fuzzy_rule(self, fuzzy_rule):
        self.fuzzy_rules.append(fuzzy_rule)

    def print_details(self):
        print("Number of rules:", len(self.fuzzy_rules))
        print("Fuzzy rules in base:")
        for rule_id in xrange(len(self.fuzzy_rules)):
            print("\n")
            self.fuzzy_rules[rule_id].print_rule()

    def evaluate(self, input_vector):
        nominator = 0
        denominator = 0
        for rule_id in xrange(len(self.fuzzy_rules)):
            nominator += self.fuzzy_rules[rule_id].degranulate_nominator(input_vector)
            denominator += self.fuzzy_rules[rule_id].degranulate_denominator(input_vector)
        if denominator != 0:
            return nominator/(3*denominator)
        return float('inf')

    def calculate_error(self, inputs, results):
        predictions = []
        # numpy nie ma MSE. Ale w scikit-learnie jest
        # Toolkit do machine learningu postawiony na numpy scipy i matplocie
        # http://scikit-learn.org/stable/index.html
        # "pip install -U scikit-learn"
        # Tak czy inaczej dupa bo nie radzi sobie z inf
        # To jest zdaje mi sie szybkie rozwiazanie
        for input_val in inputs:
            predictions.append(self.evaluate(input_val))
        error = np.array(predictions) - np.array(results)
        rss = (error * error).sum() # residual sum of squares
        mse = rss/len(predictions) # Mean squared error
        # mysle ze w obliczeniach nie ma roznicy, czy bedziemy uzywac rmse czy mse. MSE bedzie sie troche szybcziej
        # liczyc wiec zostal bym przy tym. RMSE moze byc "lepsze" przy wyswietlaniu bledu bo pokazuje o ile srednio
        # w tej samej jednostce odbiegaja przewidywania od wartosci rzeczywistych. Jak by co:
        #
        # rmse = sqrt(mse) # root mean squared error
        #
        return mse

    def change_least_weighted_rule(self, sample, new_rule):

        sorted_rules = sorted(self.fuzzy_rules, key=lambda x: x.mean_weight(sample.inputs))
        #nie wiem kurwa jak dzialaja te referencje w pythonie do konca, takze moze to tutaj nie dzialac
        sorted_rules[0] = deepcopy(new_rule)
        self.fuzzy_rules = sorted_rules


    def get_best_weighted_rule(self, sample):
        return sorted(self.fuzzy_rules, key=lambda x: x.mean_weight(sample.inputs), reverse=True)[0]
