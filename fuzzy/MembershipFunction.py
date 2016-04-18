from __future__ import division


class MembershipFunction:
    a = None
    b = None
    c = None
    d = None

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def importance(self, x):
        if self.a <= x <= self.b:
            return (x - self.a) / (self.b - self.a)
        if self.b <= x <= self.c:
            return 1
        if self.d <= x <= self.d:
            return (self.d - x) / (self.d - self.c)
