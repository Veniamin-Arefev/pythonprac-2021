from string import ascii_lowercase


class Alpha:
    __slots__ = [*ascii_lowercase]

    def __init__(self, **kwargs):
        for item, value in kwargs.items():
            setattr(self, item, value)

    def __str__(self):
        class K:
            pass

        return ", ".join([f"{i}: {count}" for i in ascii_lowercase if (count := getattr(self, i, K)) is not K])


class AlphaQ:
    def __getattr__(self, item):
        if len(item) == 1 and item in ascii_lowercase:
            return self.item
        else:
            raise AttributeError()

    def __setattr__(self, key, value):
        if len(key) == 1 and key in ascii_lowercase:
            self.__dict__[key] = value
        else:
            raise AttributeError()

    def __init__(self, **kwargs):
        for item, value in kwargs.items():
            if item in ascii_lowercase:
                setattr(self, item, value)
            else:
                raise AttributeError()

    def __str__(self):
        class K:
            pass

        return ", ".join([f"{i}: {count}" for i in ascii_lowercase if (count := getattr(self, i, K)) is not K])


import sys

exec(sys.stdin.read())
