#!/usr/bin/python3

"""
Prints methods & attributes of a class
"""


def lookup(obj):
    """
    Return a list of methods and attributes of an object

    Args:

    Return:
        list
    """
    return dir(obj)
