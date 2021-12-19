my_list = list(map(int, input().split(',')))
for i in range(len(my_list)):
    max_elem, max_elem_index = my_list[i], i
    for j in range(i, len(my_list)):
        if my_list[j] ** 2 % 100 < max_elem ** 2 % 100:
            max_elem, max_elem_index = my_list[j], j
    my_list[max_elem_index], my_list[i] = my_list[i], my_list[max_elem_index]
print(my_list)
