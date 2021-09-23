def digit_count(x):
    digit_sum = 0
    while x:
        digit_sum = x % 10
        x //= 10
    return digit_sum

n = int(input())
end = [n * n, n * (n + 1), n * (n + 2),
       (n + 1) * n, (n + 1) * (n + 1), (n + 1) * (n + 2),
       (n + 2) * n, (n + 2) * (n + 1), (n + 2) * (n + 2)]
print(n, "*", n, '=', end[0] if (digit_count(end[0]) != 6) else ':=)', sep='', end=' ')
print(n, "*", n + 1, '=', end[1] if (digit_count(end[1]) != 6) else ':=)', sep='', end=' ')
print(n, "*", n + 2, '=', end[2] if (digit_count(end[2]) != 6) else ':=)', sep='', end='\n')
print(n + 1, "*", n, '=', end[3] if (digit_count(end[3]) != 6) else ':=)', sep='', end=' ')
print(n + 1, "*", n + 1, '=', end[4] if (digit_count(end[4]) != 6) else ':=)', sep='', end=' ')
print(n + 1, "*", n + 2, '=', end[5] if (digit_count(end[5]) != 6) else ':=)', sep='', end='\n')
print(n + 2, "*", n, '=', end[6] if (digit_count(end[6]) != 6) else ':=)', sep='', end=' ')
print(n + 2, "*", n + 1, '=', end[7] if (digit_count(end[7]) != 6) else ':=)', sep='', end=' ')
print(n + 2, "*", n + 2, '=', end[8] if (digit_count(end[8]) != 6) else ':=)', sep='', end='\n')
