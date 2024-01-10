#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqs = set(my_list)
    added = 0

    for a in uniqs:
        added += a

    return (added)
