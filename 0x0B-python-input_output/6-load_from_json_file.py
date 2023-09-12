#!/usr/bin/python3

"""
Module 6-load_from_json_file docs

Function load_from_json_file creates an Object
from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a json file

    Args:
        filename - str, name of file

    Return:
        python object
    """
    with open(filename, mode="r", encoding="utf-8") as file_handle:
        return json.load(file_handle)
