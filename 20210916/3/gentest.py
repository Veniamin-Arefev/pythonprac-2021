import random
output = [random.randint(1, 100) for i in range(9)]
output.insert(random.randint(0, len(output)-1), int(input()))
print(output)