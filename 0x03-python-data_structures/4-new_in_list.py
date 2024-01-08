#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    edited = my_list[:]

    if 0 <= idx < len(my_list):
        edited[idx] = element

    return (edited)
