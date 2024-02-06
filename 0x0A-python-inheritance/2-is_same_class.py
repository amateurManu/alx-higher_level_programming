#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Function that returns True if object is of same type as
        specified class and False otherwise

    Args:
        obj: object
        a_class: the class type

    Returns:
        True if type of obj is a_class
        False if not a type
    """
    return type(obj) is a_class
