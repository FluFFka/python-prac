def decor(func):
    def newf(self, *args, **kwargs):
        print(f"{func.__name__}: {args}, {kwargs}")
        return func(self, *args, **kwargs)
    return newf

class dump(type):
    def __new__(cls, name, parents, ns):
        for k, v in ns.items():
            if callable(v):
                ns[k] = decor(v)
        return super().__new__(cls, name, parents, ns)

import sys
exec(sys.stdin.read())
