#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    size = len(my_list)
    list_cpy = [each_num for each_num in my_list]
    if (idx < 0) or (idx > (size - 1)):
        return list_cpy
    list_cpy[idx] = element
    return list_cpy
