#!/usr/bin/python3
"""

This module is composed of function that prints two new lines after '.', '?' and ':'

"""

def text_indentation(text):
    """Function that prints two new lines after . ? : characters

    Args:
        text: input string

    Returns:
        No value

    Raises:
        TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_t = s.split(d)
        s = ""
        for a in list_t:
            a = a.strip(" ")
            s = a + d if s is "" else s + "\n\n" + a + d

    print(s[:-3], end="")
