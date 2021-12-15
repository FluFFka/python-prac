import asyncio
from collections import defaultdict

async def merge(begin0, end0, begin1, end1, event_left, event_right, event_my):
    if begin1 - begin0 != 1:
        await event_left.wait()
        await event_right.wait()
    begin, i = begin0, begin0
    while begin0 < end0 and begin1 < end1:
        if L[begin0] < L[begin1]:
            LL[i] = L[begin0]
            begin0 += 1
        else:
            LL[i] = L[begin1]
            begin1 += 1
        i += 1
    await asyncio.sleep(0)
    LL[i:end1] = L[begin0:end0] + L[begin1:end1]
    L[begin:end1] = LL[begin:end1]
    event_my.set()

async def joiner():
    tasks, n = [], 0
    events = defaultdict(asyncio.Event)
    step = 2
    while step <= 2 * len(L):
        for i in range(0, len(L), step):
            left_begin = i
            left_end = i + step // 2
            right_begin = i + step // 2
            right_end = min(i + step, len(L))
            if left_end >= len(L):
                events[(i, len(L))].set()
                continue
            event_left = events[(left_begin, left_end)]
            event_right = events[(right_begin, right_end)]
            if step == 2:
                event_left.set()
                event_right.set()
            event_my = events[(left_begin, right_end)]
            tasks.append(asyncio.create_task(merge(left_begin, left_end, right_begin, right_end, event_left, event_right, event_my)))
        step *= 2
    await asyncio.gather(*tasks)


L = eval(input())
LL = [0] * len(L)
asyncio.run(joiner())
print(L)
