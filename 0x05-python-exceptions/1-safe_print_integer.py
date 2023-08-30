#!/usr/bin/python3


def safe_print_integer(value):

    try:
        numeric_value = int(value)
        print("{:d}".format(numeric_value))
        return True
    except ValueError:
        return False
