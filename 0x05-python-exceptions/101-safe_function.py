#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error_message:
        print("Exception: {}\n".format(error_message))
        return None
