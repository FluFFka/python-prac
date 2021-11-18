def check_type(t):
    def decor(f):
        def newf(*args):
            if any(type(par) is not t for par in args):
                raise TypeError(f"Not {t}")
            return f(*args)
        return newf
    return decor

@check_type(str)
def fun(a, b):
    return a*2+b


