print([i for i in range(*map(int, input().split(','))) if ([i % j == 0 for j in range(1, i + 1)].count(True) == 2)])
