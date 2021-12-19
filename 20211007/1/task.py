def Pareto(*my_li):
    if len(my_li) > 2:
        dom = [i for i in my_li if
               any([(i[0] < j[0] and i[1] <= j[1]) or (i[0] <= j[0] and i[1] < j[1]) for j in my_li])]
        return tuple(i for i in my_li if i not in dom)
    else:
        return (my_li,)


print(Pareto(*eval(input())))
