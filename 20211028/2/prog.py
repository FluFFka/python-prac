from itertools import islice
def slide(seq, n):
    i = 0
    while 1:
        # seqcopy = seq
        curr = list(islice(seq, i, i+n))
        if len(curr) < n:
            break
        yield from curr
        i += 1
# next(I, None)
from time import sleep
def f():
    i = 0
    while True:
        yield i
        i += 1
s = slide(f(), 5)
while True:
    sleep(0.1)
    print('\t', next(s))
