#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    keys_list = list(new.keys())

    for a in keys_list:
        new[a] *= 2

    return (new)
