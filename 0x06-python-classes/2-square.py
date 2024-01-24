#!/usr/bin/python3
"""Defines square based on 1-square.py
"""
class Square:
    """Class that defines a square by its size
    """
    def __init__(self, size=0):
        """Method to initialize square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
