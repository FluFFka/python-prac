import random
import asyncio


L = list(range(16))
random.shuffle(L)
LL = L.copy()


# [ 1, 2, 3, 4, [7, 8], [5, 6], ... ]
async def merge(b0, b1, e1, event_left, event_right, my_event):
    if b1 - b0 != 1:
        await event_left.wait()
        await event_right.wait()
    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(random.randint(0, 2) / 10) # asyncio.sleep(0)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    
    my_event.set()

async def joiner():
    tasks, n = [], 0
    events = dict() # defaultdict(asyncio.Event)
    for p in range(4):
        b = 2**(p + 1)
        for i in range(0, len(L), b):
            events[(i, i + b)] = asyncio.Event()
            if b == 2:
                event_left = None
                event_right = None
            else:
                event_left = events[(i, i + b // 2)]
                event_right = events[(i + b // 2, i + b)]
            my_event = events[(i, i + b)]
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, event_left, event_right, my_event)))
    await asyncio.gather(*tasks)

print(L)
asyncio.run(joiner())
print(L)
