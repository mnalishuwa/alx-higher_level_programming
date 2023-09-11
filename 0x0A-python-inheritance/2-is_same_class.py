#!/usr/bin/python3

"""
check if object is instance of a given class
"""


def is_same_class(obj, a_class):
    """
    check if object is an instance of a class
    """
    if type(obj) == a_class:
        return True
    return False
