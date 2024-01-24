#!/usr/bin/python3
"""Defines a class Square based on 2-square.py
"""
class Square:
    """A class defining a square by its size
    """
    def __init__(self, size=0):
        """Method to initialize square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that returns the current square area
        """
        return (self.__size ** 2)
