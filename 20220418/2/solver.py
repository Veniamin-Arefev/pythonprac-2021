class SquareIO:
    @staticmethod
    def inputCoeff(name):
        return input(f'Input {name}:')

    @staticmethod
    def printResult(result):
        return print(f'Solution: {result}')


def solveSquare(a, b, c):
    if a != 0:
        d = b * b - 4 * a * c
        if d >= 0:
            x1, x2 = -b + d ** 0.5 / 2 * a, -b - d ** 0.5 / 2 * a
            return x1, x2
        else:
            return None
    elif b != 0:
        return -c / b
    elif c != 0:
        return None
    else:
        return 100500


def main():
    inp = []
    for item in ['a', 'b', 'c']:
        inp.append(float(SquareIO.inputCoeff(item)))
    answer = solveSquare(*inp)
    SquareIO.printResult(answer)


if __name__ == "__main__":
    main()
