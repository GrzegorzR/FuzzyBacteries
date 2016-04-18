from MembershipFunction import MembershipFunction


class FuzzyRule:
    antecedents = None
    consequence = None

    def __init__(self, inpusts):
        self.antecedents = [MembershipFunction(0, 0, 0, 0) for i in xrange(inpusts)]
        self.consequence = MembershipFunction(0, 0, 0, 0)
