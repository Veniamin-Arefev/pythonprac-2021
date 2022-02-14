import zlib
import sys

with open(sys.argv[1], 'rb') as file:
    print(zlib.decompress(file.read()))

