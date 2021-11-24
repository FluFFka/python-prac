from string import ascii_lowercase

class Alpha:
    __slots__ = [*ascii_lowercase]
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        return ', '.join([f"{key}: {getattr(self, key)}" for key in self.__slots__ if hasattr(self, key)])

class EMPTYCLASS: pass

class AlphaQ(EMPTYCLASS):
    def __init__(self, **kwargs):
        if not all(key in ascii_lowercase for key in kwargs):
            raise AttributeError
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __setattr__(self, key, value):
        if key in ascii_lowercase:
            super().__setattr__(key, value)
        else:
            raise AttributeError
    def __str__(self):
        return ', '.join([f"{key}: {getattr(self, key)}" for key in ascii_lowercase if hasattr(self, key)])

import sys
exec(sys.stdin.read())
