import itertools


def slide(seq, n):
    seq = itertools.tee(seq, 2)
    yield from itertools.islice(seq[0], n)
    while next(seq[1], None) is not None:
        seq = itertools.tee(seq[1], 2)
        yield from itertools.islice(seq[0], n)


import sys

exec(sys.stdin.read())
# it = 0
# for i in slide(itertools.count(0), 5):
#     print(i, end=" ")
#     if (it := it + 1) > 100:
#         break
