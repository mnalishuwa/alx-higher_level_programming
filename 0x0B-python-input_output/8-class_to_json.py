#!/usr/bin/python3

"""
Module 8-class_to_json docs

Function class_to_json returns the dictionary
description with simple data structure for
JSON serialization of an object
"""


def class_to_json(obj):
    """
    Return data structure for json serialization

    Args:
        obj - class object

    Return:
        dict - description of class obj
    """
    return {attr: getattr(obj, attr) for attr in dir(obj)
            if not callable(getattr(obj, attr)) and not attr.startswith("__")}
