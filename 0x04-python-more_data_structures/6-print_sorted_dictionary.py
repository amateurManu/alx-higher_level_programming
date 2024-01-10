#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary)
    for a in a_dictionary:
        print("{}: {}".format(a, a_dictionary.get(a)))
