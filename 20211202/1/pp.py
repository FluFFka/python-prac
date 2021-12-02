class ctype(type):

    def __call__(self, *args, **kwargs):
        print("call", self, args, kwargs)
        return super().__call__(*args, **kwargs)

    def __new__(cls, name, parents, ns):
        print("new", cls, name, parents, ns)
        return super().__new__(cls, name, parents, ns)

    def __init__(self, name, parents, ns):
        print("init", self, parents, ns)
        return super().__init__(name, parents, ns)

class C(int, metaclass=ctype):
     field = 42

