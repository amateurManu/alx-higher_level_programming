#!/usr/bin/python3
"""Defines a class Square based on 3-square.py
"""
class Square:
    """A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Method initializing square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that returns square of object
        """
        return (self.__size ** 2)

    @prpoerty
    def size(self):
        """Method to return size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set value of square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
