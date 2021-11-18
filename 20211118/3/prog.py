import string
import time
# string.ascii_lowercase
# time.time()

class Alpha:
    __slots__ = [*string.ascii_lowercase]
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
