import struct
import sys

try:
    inp = sys.stdin.buffer.read(44)
    f = "4cI4c4cIHHIIHH4cI"
    kek = struct.unpack(f, inp)

    if b"".join(kek[0:4]) != b"RIFF" or b"".join(kek[5:9]) != b"WAVE" or \
            b"".join(kek[9:13]) != b"fmt " or b"".join(kek[20:24]) != b"data":
        raise ValueError("ERROR!!!")

    print(f"Size={kek[4]}, Type={kek[14]}, Channels={kek[15]}, Rate={kek[16]}, Bits={kek[19]}, Data size={kek[24]}")
except Exception as e:
    print("NO")
