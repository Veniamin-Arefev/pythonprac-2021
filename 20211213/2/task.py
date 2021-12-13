import random
import asyncio
import math

random.shuffle(L := [*range(32)])
LL = L.copy()


async def merge(start1, start2, stop2, *, left_event, right_event, end_event):
    # print(f"wait for {(start1, start2)} and {(start2, stop2)}")
    await asyncio.gather(left_event.wait(), right_event.wait())
    # print(f"got for {(start1, start2)} and {(start2, stop2)}")

    b, stop1, i = start1, start2, start1
    while start1 < stop1 and start2 < stop2:
        if L[start1] < L[start2]:
            LL[i] = L[start1]
            start1 += 1
        else:
            LL[i] = L[start2]
            start2 += 1
        i += 1

    await asyncio.sleep(0)

    LL[i:stop2] = L[start1:stop1] + L[start2:stop2]
    L[b:stop2] = LL[b:stop2]

    end_event.set()


async def joiner():
    old_len, new_len = len(L), pow(2, math.ceil(math.log2(len(L))))
    if (new_len > old_len):
        L.extend([0 for i in range(new_len - old_len)])
        print(len(L))
    events = {(i, i + 2 ** (p),): asyncio.Event()
              for p in range(5)
              for i in range(0, len(L), 2 ** (p))}
    # print(events.keys())
    tasks = []
    for p in range(4):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b,
                                                   left_event=events[(i, i + b // 2,)],
                                                   right_event=events[(i + b // 2, i + b,)],
                                                   end_event=events[(i, i + b,)])))
            # left_event=(i, i + b // 2,),
            # right_event=(i, i + b,),
            # end_event=(i, i + b,))))
            # print(i, i + b // 2, i + b)

    for i in range(0, len(L), 2):
        events[(i, i + 1,)].set()
        events[(i + 1, i + 2,)].set()
        # print(i, i + 1, i + 2)
    await asyncio.gather(*tasks)


L = eval(input())
asyncio.run(joiner())
print(L)
