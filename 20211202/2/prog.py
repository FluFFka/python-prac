def check_annotations(self):
    if hasattr(self, "__annotations__"):
        for attr, req_type in self.__annotations__.items():
            if not hasattr(self, attr) or \
                    not isinstance(getattr(self, attr), req_type):
                return False
    return True

class check(type):
    def __new__(cls, name, parents, ns):
        ns['check_annotations'] = check_annotations
        return super().__new__(cls, name, parents, ns)

import sys
exec(sys.stdin.read())

