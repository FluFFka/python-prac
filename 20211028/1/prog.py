def fib(m, n):
    fib1, fib2 = 1, 1
    for i in range(n + 1):
        if i >= m:
            yield fib1
        fib1, fib2 = fib2, fib1 + fib2

import sys
exec(sys.stdin.read())
