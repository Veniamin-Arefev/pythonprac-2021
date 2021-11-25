import sys

inp = sys.stdin.buffer.read()

parts = []

for i in range(inp[0]):
    parts.append(inp[int(i * (len(inp) - 1) / inp[0]):int((i + 1) * (len(inp) - 1) / inp[0])])

parts.sort()

sys.stdout.buffer.write(inp[0:1] + b''.join(parts))
