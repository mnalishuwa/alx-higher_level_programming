#!/usr/bin/python3

"""
Module 0-read_file

Function reads and prints contents from txt file
"""


def read_file(filename=""):

    """
    read_file - opens and reads filename(txt) and prints to stdout

    Arguments:
        filename - str, name of file

    Return:
        None
    """
    with open(filename, "r") as file_handler:
        for line in file_handler:
            print(line, end="")
