import math

my_fun = {}
calculated = 0
while a := input():
    my_list = a.split(" ")
    if my_list[0] == "quit":
        break
    elif my_list[0][0] == ":":  # new func
        my_fun[my_list[0][1:]] = my_list[1:]
    else:  # command
        # print(my_fun[my_list[0]][-1])
        # print({my_fun[my_list[0]][ind]: eval(my_list[1 + ind]) for ind in range(len(my_list) - 1)})
        print(eval(my_fun[my_list[0]][-1], math.__dict__,
                   {my_fun[my_list[0]][ind]: eval(my_list[1 + ind]) for ind in range(len(my_list) - 1)}))
    calculated += 1
print(("{}:{}" if len(my_list) < 2 else eval(my_list[1])).format(len(my_fun) + 1, calculated + 1))
