inp = input()
print(len({inp[i:i + 2].lower() for i in range(len(inp)) if inp[i:i + 2].isalpha()}))
