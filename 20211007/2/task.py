def SUB(list1, list2):
    if type(list1) in [list, tuple]:
        return type(list1)([j for j in list1 if j not in list2])
    else:
        return list1 - list2


print(SUB(*eval(input())))
