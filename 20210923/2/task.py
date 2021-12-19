my_sum = 0
while my_sum <= 21:
    a = int(input())
    if a > 0:
        my_sum += a
    else:
        break
print(my_sum if my_sum > 21 else a)
