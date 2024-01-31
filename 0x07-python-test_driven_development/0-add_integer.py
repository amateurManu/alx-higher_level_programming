#!/usr/bin/python3
"""

This module is composed of a function that adds two numbers

"""

def add_integer(a, b=98):
    """ Function that adds two integers and also floats

    Args:
        a: first number
        b: second number

    Returns:
        The addition of given numbers

    Raises:
        TypeError: if a or b are not integer or float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
