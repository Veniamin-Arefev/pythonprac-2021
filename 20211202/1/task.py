from functools import wraps


def my_dumper(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f'{f.__name__}: {args[1:]}, {kwargs}')
        return f(*args, **kwargs)

    return wrapper


class dump(type):
    def __init__(self, name, parents, ns):
        for key, value in self.__dict__.items():
            if callable(value):
                setattr(self, key, my_dumper(value))
        return super().__init__(name, parents, ns)


import sys

exec(sys.stdin.read())
