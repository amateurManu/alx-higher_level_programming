#!/usr/bin/python3
def no_c(my_string):
    b = 0

    edited = my_string[:]

    for a in range(len(my_string)):
        if (my_string[a] == 'c' or my_string[a] == 'C'):
            edited = edited[:(a - b)] + edited[(a + 1):]
            b += 1

    return (edited)
