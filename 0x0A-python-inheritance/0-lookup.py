#!/usr/bin/python3
def lookup(obj):
    """ Function that returns list of available attributes and
        methods of an object

    Args:
        obj: class instance

    Returns:
        List of attributes
    """

    return dir(obj)
