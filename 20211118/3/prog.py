from string import ascii_lowercase

al = [*ascii_lowercase]


class Alpha:
    __slots__ = al
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        return ', '.join([f"{key}: {getattr(self, key)}" for key in self.__slots__ if hasattr(self, key)])


class AlphaQ:
    def __init__(self, **kwargs):
        for key in kwargs:
            if not (key in al):
                raise AttributeError(f"'AlphaQ' object has no attribute '{key}'")
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __setattr__(self, key, value):
        if key in al:
            super().__setattr__(key, value)
        else:
            raise AttributeError(f"'AlphaQ' object has no attribute '{key}'")
    def __str__(self):
        return ', '.join([f"{key}: {getattr(self, key)}" for key in al if hasattr(self, key)])

import sys
exec(sys.stdin.read())
