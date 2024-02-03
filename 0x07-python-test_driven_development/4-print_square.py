#!/usr/bin/python3
"""
This module is composed of a function that prints a square with #

"""

def print_square(size):
    """ Function that prints a square of character #

    Args:
        size: size of square needed to be printed

    Returns:
        No value

    Raises:
        TypeError: If size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        print("#" * size)
