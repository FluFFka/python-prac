def dumpc(cls):
    class newcl(cls):
        def __str__(self):
            res = super().__str__()
            return f">>>{res}<<<"
    return newcl

@dumpc
class A(str): pass


