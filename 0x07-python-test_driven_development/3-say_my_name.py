#!/usr/bin/python3

"""
Function prints out strings passed
"""


def say_my_name(first_name, last_name=""):
    """
    Prints string passed to it

    Arguments:
        first_name - str
        last_name - str

    Raises:
        TypeError - if first_name or last_name not str

    Return:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
