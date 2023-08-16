#!/usr/bin/python3


def search_replace(my_list, search, replace):

    result = [ea if ea != search else replace for ea in my_list]
    return result
