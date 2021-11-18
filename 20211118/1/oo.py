def check_int(f):
    def newf(*args):
        for par in args:
            if not (type(par) is int):
                raise TypeError("not int")
        return f(*args)
    return newf


@check_int
def fun(a, b):
    return a*2+b


