class Num:
    def __get__(self, instance, owner):
        return getattr(instance, "_val", 0)

    def __set__(self, instance, value):
        instance._val = re if (re := getattr(value, "real", None)) is not None else len(value)


import sys

exec(sys.stdin.read())
