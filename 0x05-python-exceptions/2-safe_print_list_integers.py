#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    elements_printed = 0
    for index in range(x):
        try:
            element = my_list[index]
            value = int(element)
            print("{:d}".format(value), end="")
            elements_printed += 1
        except (ValueError, TypeError):
            continue
    return elements_printed
