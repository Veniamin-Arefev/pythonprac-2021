my_sum = 0
while a := int(input()):
    if a > 0 and my_sum <= 21:
        my_sum += a
    else:
        break
print(my_sum if my_sum > 21 else a)
