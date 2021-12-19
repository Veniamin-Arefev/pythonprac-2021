def objcount(cls):
    class newcls(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            type(self).counter += 1
            super().__init__()
            pass

        def __del__(self):
            if hasattr(cls, "__del__"):
                super().__del__()
            type(self).counter -= 1

    return newcls


import sys

exec(sys.stdin.read())
