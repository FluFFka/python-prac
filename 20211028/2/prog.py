from itertools import islice
from itertools import tee
def slide(seq, n):
    seqcopy = seq
    while 1:
        seqcopy, seq = tee(seqcopy)
        curr = list(islice(seq, n))
        if len(curr) < n:
            break
        yield from curr
        next(seqcopy)

import sys
exec(sys.stdin.read())

