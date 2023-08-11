#!/usr/bin/python3


def remove_char_at(str, n):

    index = n
    if n < 0 or n >= len(str):
        return str
    new_str = ""
    for index in range(len(str)):
        if index == n:
            continue
        new_str += str[index]
    return new_str
