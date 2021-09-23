number = int(input())
print('A', '+' if number % 25 == 0 and number % 2 == 0 else '-',
      'B', '+' if number % 25 == 0 and number % 2 != 0 else '-',
      'C', '+' if number % 8 == 0 else '-')
