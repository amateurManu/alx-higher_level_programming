#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    output = []

    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            output.append(True)
        else:
            output.append(False)

    return (output)
