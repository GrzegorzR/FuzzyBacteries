from math import sin, cos
from random import uniform
from data.Data import DataSample


def function2d(x1, x2):
    return sin(x1) + cos(x2)


def get_2d_sample(number):
    inputs = []
    outputs = []
    in_rang = [(0,6), (0,6)]
    out_rang = (-5,5)
    for i in xrange(0, number):
        x1, x2 = uniform(in_rang[0][0], in_rang[0][1]), uniform(in_rang[1][0], in_rang[1][1])
        outputs.append(function2d(x1, x2))
        inputs.append((x1,x2))
    return DataSample(inputs, outputs, in_rang, out_rang)
