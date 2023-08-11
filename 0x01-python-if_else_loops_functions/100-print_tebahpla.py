#!/usr/bin/python3

for ascii_int in range(122, 96, -1):
    if ascii_int % 2 == 1:
        res = ascii_int - 32
    else:
        res = ascii_int
    print("{}".format(chr(res)), end="")
