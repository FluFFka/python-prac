class Num:
    def __get__(self, obj, cls):
        if hasattr(obj, "_val"):
            return obj._val
        return 0
    def __set__(self, obj, value):
        if hasattr(value, "real"):
            obj._val = value
        else:
            obj._val = len(list(value))
    def __delete__(self, obj):
        obj._val = 0
        pass

import sys
exec(sys.stdin.read())
