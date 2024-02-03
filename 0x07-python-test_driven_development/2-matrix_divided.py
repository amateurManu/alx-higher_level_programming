#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""

def matrix_divided(matrix, div):
    """ Function that divides the integer/ float of a matrix

    Args:
        matrix: list of a lists of integers and/or floats
        div: number dividing the matrix

    Returns:
        A new matrix with the result of division

    Raises:
        TypeError:
            If the elements of matrix are not lists
            If elements of lists are not integers/floats
            If div is not an integer/number
            If the lists of the matrix do not have the same size

        ZeroDivisionError: 
            If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_t = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_t)

    len_e = 0
    msg_s = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msg_t)

        if len_e != 0 and len(elements) != len_e:
            raise TypeError(msg_s)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(msg_t)

        len_e = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
