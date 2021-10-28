import itertools

print(*sorted(filter(lambda x: x.count("TOR") == 2, map(lambda x: ''.join(x), itertools.product('TOR', repeat=int(input()))))))
