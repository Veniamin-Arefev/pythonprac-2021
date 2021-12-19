class Num:
    def __get__(self, instance, owner):
        return getattr(instance, "_val", 0)

    def __set__(self, instance, value):
        instance._val = value if (hasattr(value, "real")) else len(value)


import sys

exec(sys.stdin.read())
