#!/usr/bin/python3

"""
add_integer function adds 2 numbers (floats or ints)
"""


def add_integer(a, b=98):
    """
    Integer addition function

    Arguments:
        a (int, float)
        b (int, float)

    Attributes:

    Raises:
        TypeError

    Return:
        a + b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
