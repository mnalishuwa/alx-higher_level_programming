#!/usr/bin/python3


def max_integer(my_list=[]):

    size = len(my_list)
    if size == 0:
        return None
    largest = my_list[0]
    for each_int in my_list:
        if each_int > largest:
            largest = each_int
    return largest
