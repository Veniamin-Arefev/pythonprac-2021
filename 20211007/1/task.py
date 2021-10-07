def Pareto(*my_li):
    dom = [i for i in my_li if any([(i[0] < j[0] and i[1] <= j[1]) or (i[0] <= j[0] and i[1] < j[1]) for j in my_li])]
    return [i for i in my_li if i not in dom]


print(Pareto(*eval(input())))
