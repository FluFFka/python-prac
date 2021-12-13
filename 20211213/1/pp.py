import random
import asyncio


L = list(range(16))
random.shuffle(L)
LL = L.copy()


# [ 1, 2, 3, 4, [7, 8], [5, 6], ... ]
async def merge(b0, b1, e1, n):
    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0)
    print(f"> {n}")
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]


async def joiner():
    tasks, n = [], 0
    for p in range(4):
        b = 2**(p + 1)
        for i in range(0, len(L), b):
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n)))
            n += 1
    await asyncio.gather(*tasks)

print(L)
asyncio.run(joiner())
print(L)
