#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    #first = my_list[0]

    for biggest in range(1, len(my_list)):
        if my_list[biggest] > my_list[0]:
            my_list[0] = my_list[biggest]

    return (my_list[0])
