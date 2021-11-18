def objcount(cls):
    class newcls(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            type(self).counter += 1
            super().__init__(*args, **kwargs)
            pass

        def __del__(self):
            type(self).counter -= 1

    return newcls


import sys

exec(sys.stdin.read())
