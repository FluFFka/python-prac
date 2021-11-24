def objcount(cl):
    class newclass(cl):
        counter = 0
        def __init__(self, *args, **kwargs):
            try:
                super().__init__(*args, **kwargs)
            except:
                super().__init__()
            self.__class__.counter += 1
        def __del__(self):
            self.__class__.counter -= 1
            if hasattr(super(), "__del__"):
                super().__del__()
    return newclass

import sys
exec(sys.stdin.read())

