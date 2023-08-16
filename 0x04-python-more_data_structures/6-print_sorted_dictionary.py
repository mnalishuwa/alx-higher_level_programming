#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    for each_key in sorted(a_dictionary.keys()):
        print(each_key, ": ", a_dictionary[each_key], sep="")
