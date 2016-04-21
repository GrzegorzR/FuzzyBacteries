from math import exp
from random import uniform
from data.Data import DataSample


def function6d(x1, x2, x3, x4, x5, x6):
    return x1 + x2 ** 0.5 + x3 * x4 + 2 * exp(x5 + x6)


def get_6dsample(number):
    inputs = []
    outputs = []
    in_rang = [(1, 5), (1, 5), (0, 4), (0, 0.6), (0, 1), (0, 1.2)]
    out_rang = (3.9, 27.5)
    for i in xrange(0, number):
        x1, x2 = uniform(in_rang[0][0], in_rang[0][1]), uniform(in_rang[1][0], in_rang[1][1])
        x3, x4 = uniform(in_rang[2][0], in_rang[2][1]), uniform(in_rang[3][0], in_rang[3][1])
        x5, x6 = uniform(in_rang[4][0], in_rang[4][1]), uniform(in_rang[5][0], in_rang[5][1])
        inputs.append((x1, x2, x3, x4, x5, x6))
        outputs.append(function6d(x1, x2, x3, x4, x5, x6))
    return DataSample(inputs, outputs, in_rang, out_rang)
