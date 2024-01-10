#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = 0
    keys_list = list(a_dictionary.keys())

    for a in keys_list:
        keys += 1

    return (keys)
