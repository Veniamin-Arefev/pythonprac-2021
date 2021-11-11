class InvalidInput(Exception):
    string = 'Invalid input'

    def __str__(self):
        return self.string


class BadTriangle(Exception):
    string = 'Not a triangle'

    def __str__(self):
        return self.string


def triangleSquare(string):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(string)
    except Exception as e:
        raise InvalidInput
    sides = [((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5,
             ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5]
    area_square = ((p := sum(sides) / 2) * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
    if area_square.imag != 0 or area_square.real <= 0:
        raise BadTriangle
    else:
        return area_square


while True:
    try:
        square = triangleSquare(input())
    except (InvalidInput, BadTriangle) as e:
        print(e)
    else:
        print(f"{square.real:.2f}")
        break
