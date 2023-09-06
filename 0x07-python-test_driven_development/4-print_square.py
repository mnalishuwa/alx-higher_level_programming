#!/usr/bin/python3

"""
Print square function
"""


def print_square(size):
    """
    Function prints square using # symbol

    Arguments:
        size - int

    Raises:
        TypeError - if size not int
        ValueError - size < 0

    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
