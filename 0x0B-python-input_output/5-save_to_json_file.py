#!/usr/bin/python3

"""
Module 5-save_to_json_file docs

Function save_to_json_file writes an Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write my_obj to filename

    Args:
        my_obj - string object
        filename - string, name of file

    Return:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file_handle:
        json.dump(my_obj, file_handle)
