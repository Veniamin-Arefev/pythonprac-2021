def solveSquare(a, b, c):
    d = b * b - 4 * a * c
    if d >= 0:
        x1, x2 = -b + d ** 0.5 / 2 * a, -b - d ** 0.5 / 2 * a
        return x1, x2
    else:
        return None
