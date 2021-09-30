my_list = list(map(int, input().split(',')))
for i in range(len(my_list)):
    max_elem = my_list[i]
    for j in range(i, len(my_list)):
        if my_list[j] ** 2 % 100 < max_elem ** 2 % 100:
            max_elem = my_list[j]
    my_list[my_list.index(max_elem)], my_list[i] = my_list[i], my_list[my_list.index(max_elem)]
print(my_list)