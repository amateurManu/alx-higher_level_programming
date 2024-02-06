#!/usr/bin/python3
""" This module contains a function that reads from a file """

def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises:
        Exception: when file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        data_read = f.read()
        print(data_read, end='')
