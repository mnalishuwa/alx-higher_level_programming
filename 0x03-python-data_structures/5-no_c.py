#!/usr/bin/python3


def no_c(my_string):

    result = ""
    for each_char in my_string:
        if each_char in "cC":
            continue
        result += each_char
    return result
