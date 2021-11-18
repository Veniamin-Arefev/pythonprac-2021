def decclass(cls):
    class newcls(cls):
        created_count = 0
        alive_count = 0

        def __init__(self, *args, **kwargs):
            print(args, kwargs)
            type(self).created_count += 1
            type(self).alive_count += 1
            print("created new")
            super().__init__()
            pass

        def __del__(self):
            type(self).alive_count -= 1
            print("deleted")
    return newcls

@decclass
class Kek(str):
    pass

a = Kek("123")
print(Kek.created_count)
print(Kek.alive_count)
b = Kek("456")
print(Kek.created_count)
print(Kek.alive_count)
c = Kek("987")
print(Kek.created_count)
print(Kek.alive_count)
del a
print(Kek.created_count)
print(Kek.alive_count)
del b
print(Kek.created_count)
print(Kek.alive_count)