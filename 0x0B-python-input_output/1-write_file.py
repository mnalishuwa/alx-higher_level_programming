#!/usr/bin/python3

"""
Module 1-write_file

Function write a string at the end of a text file,
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    append_write - appends to txt file

    Args:
        filename - str, filename
        text - str, data to be appended to txt

    Return:
        int - number of characters appended
    """
    with open(filename, "w", encoding="utf-8") as file_handler:
        num_characters = file_handler.write(text)
        return num_characters
