from math import *

*ints, fun = input().split()
width, height, A, B = map(int, ints)

mul = 4
y = [A + i * (B - A) / (mul * width - 1) for i in range(mul * width)]
x = [eval(fun.replace('x', str(i))) for i in y]

x_dot = [round(abs((A - i) / (A - B) * (width - 1))) for i in y]
y_dot = [round(abs((max(x) - i) / (max(x) - min(x))) * (height - 1)) for i in x]

output = [[' ' for i in range(width)] for j in range(height)]

for x_cor, y_cor in enumerate(y_dot):
    output[y_cor][x_dot[x_cor]] = "*"

for y_ind, y in enumerate(output):
    for x_ind, x in enumerate(y):
        if x_ind > 0 and y_ind > 0:
            if output[y_ind - 1][x_ind] == "*" and output[y_ind][x_ind - 1] == "*" and output[y_ind][x_ind] == "*":
                output[y_ind][x_ind] = " "
for y_ind, y in enumerate(output):
    for x_ind, x in enumerate(y):
        if x_ind + 1 < len(y) and y_ind > 0:
            if output[y_ind - 1][x_ind] == "*" and output[y_ind][x_ind + 1] == "*" and output[y_ind][x_ind] == "*":
                output[y_ind][x_ind] = " "


for i in output:
    print(*i, sep="")
