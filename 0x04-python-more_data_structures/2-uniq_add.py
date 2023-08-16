#!/usr/bin/python3


def uniq_add(my_list=[]):

    uniques = {}
    total = 0
    for each_int in my_list:
        uniques[each_int] = uniques.get(each_int, 0) + 1
        if uniques[each_int] == 1:
            total += each_int
    return total
