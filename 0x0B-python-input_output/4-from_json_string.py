#!/usr/bin/python3


"""
Module 4-from_json_string docs

Function from_json_string returns python object from
json string representation
"""

import json


def from_json_string(my_str):
    """
    Function returns obj from json string

    Args:
        my_str - json string representation

    Return:
        python object
    """
    return json.loads(my_str)
