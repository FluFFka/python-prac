class D:
    def __get__(self, obj, cls):
        print("get")
        return obj._val
    def __set__(self, obj, value):
        obj._val = value
        print("set")
        return
    def __delete__(self, obj):
        obj._val = None
        print("AAAAA")

class C:
    d = D()
