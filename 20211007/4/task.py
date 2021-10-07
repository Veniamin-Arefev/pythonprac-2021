from math import *


def Calc(s, t, u):
    return lambda x: (lambda x, y: eval(u))((lambda x: eval(s))(x), (lambda x: eval(t))(x))


F = Calc(*eval(input()))
print(F(eval(input())))
