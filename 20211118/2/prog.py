class Num:

    def __get__(self, obj, cls):
        try:
            return obj._val
        except Exception:
            return 0
    def __set__(self, obj, value):
        try:
            value.real
            obj._val = value
        except Exception:
            obj._val = len(value)

import sys
exec(sys.stdin.read())
