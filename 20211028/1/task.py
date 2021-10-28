import itertools


def my_fib():
    a, b = 1, 1
    yield 1
    yield 1
    while True:
        yield a + b
        a, b = b, a + b


def fib(m, n):
    yield from itertools.islice(my_fib(), m, n + 1)


print(", ".join([str(i) for i in fib(2, 4)]))
