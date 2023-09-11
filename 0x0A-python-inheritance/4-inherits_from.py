#!/usr/bin/python3

"""
Check if object is subclass of a class
"""


def inherits_from(obj, a_class):
    """
    Return true is obj is subclass of a_class

    Args:
        obj - object
        a_class - class_name

    Return:
        bool
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
