from string import ascii_lowercase


class Alpha:
    __slots__ = [*ascii_lowercase]

    def __init__(self, **kwargs):
        for item, value in kwargs.items():
            setattr(self, item, value)

    def __str__(self):
        class K: pass

        return " ".join([f"{i}: {count}" for i in ascii_lowercase if (count := getattr(self, i, K)) is not K])


import sys

exec(sys.stdin.read())
