def Bisect(item, my_list):
    if my_list[len(my_list) // 2] == item:
        return True
    if len(my_list) == 1:
        return False
    if my_list[len(my_list) // 2] < item:
        return Bisect(item, my_list[len(my_list) // 2 + len(my_list) % 2:])
    else:
        return Bisect(item, my_list[:len(my_list) // 2])


print(Bisect(*eval(input())))
