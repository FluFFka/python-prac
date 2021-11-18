def dump(fn):
    def newf(*args, **kwargs):
        print("->", args, kwargs)
        res = fn(*args, **kwargs)
        print("<-", res)
        return res
    return newf

@dump
def fun(a, b):
    return a*2+b

