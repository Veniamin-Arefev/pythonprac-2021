class OrderedComplex(complex):
    real = 0
    imagine = 0

    def __init__(self, real=0, imagine=0):
        self.real = real
        self.imagine = imagine

    def __lt__(self, other):
        return self.real < other.real and self.imagine < other.imagine


class OrderedComplexMul(OrderedComplex):
    def __matmul__(self, other):
        return self.real * other.real + self.imagine * other.imagine



import sys

exec(sys.stdin.read())
