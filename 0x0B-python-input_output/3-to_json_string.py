#!/usr/bin/python3

"""
Module 3-to_json_string docs

Function to_json_string returns JSON representation
of a string object
"""


import json


def to_json_string(my_obj):
    """
    return JSON representation of an object

    Args:
        my_obj - string object

    Return:
        json object
    """
    return json.dump(my_obj)
