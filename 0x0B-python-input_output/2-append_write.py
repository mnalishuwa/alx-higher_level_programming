#!/usr/bin/python3

"""
Module 2-append_write

Function appends a string at the end of a text file,
returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    append_write - appends to txt file

    Args:
        filename - str, filename
        text - str, data to be appended to txt

    Return:
        int - number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as file_handler:
        num_characters = file_handler.write(text)
        return num_characters
