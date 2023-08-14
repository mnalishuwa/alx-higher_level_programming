#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    size = len(my_list)

    if (size == 0) or (idx < 0) or (idx > (size - 1)):
        return my_list

    for index in range(idx, size - 1):
        my_list[index] = my_list[index + 1]

    my_list[:] = my_list[:-1]
    return my_list
