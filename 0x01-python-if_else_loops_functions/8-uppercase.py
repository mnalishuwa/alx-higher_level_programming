#!/usr/bin/python3


def uppercase(str):

    for each_char in str:
        if (ord(each_char) >= 97 and ord(each_char) < 123):
            res_char = chr(ord(each_char) - 32)
        else:
            res_char = each_char
        print(res_char, end="")
    print()
