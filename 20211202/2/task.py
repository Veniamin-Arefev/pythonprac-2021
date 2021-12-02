def check_annotations(cls: object):
    mas = [hasattr(cls, f_name) and isinstance(getattr(cls, f_name), f_type)
           for f_name, f_type in cls.__annotations__.items()]
    return all(mas)


class check(type):

    def __init__(self, name, parents, ns):
        setattr(self, 'check_annotations', check_annotations)
        return super().__init__(name, parents, ns)


import sys

exec(sys.stdin.read())
