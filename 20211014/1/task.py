from fractions import Fraction

# noinspection PyTypeChecker
my_input = list(map(Fraction, input().split(",")))

A_cof = [my_input[i] for i in range(3, 3 + 1 + my_input[2].numerator)]
B_cof = [my_input[i] for i in range(3 + 2 + my_input[2].numerator, len(my_input))]

A = sum([my_input[0] ** (len(A_cof) - index - 1) * cof for index, cof in enumerate(A_cof)])
B = sum([my_input[0] ** (len(B_cof) - index - 1) * cof for index, cof in enumerate(B_cof)])

print(True if B != 0 and A / B == my_input[1] else False)
