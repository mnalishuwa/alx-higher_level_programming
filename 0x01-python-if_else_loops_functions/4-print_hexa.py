#!/usr/bin/python3


def _hex(number):

    base_chars = "0123456789abcdef"
    prefix = "0x"
    base = 16

    floor_ceil = (number // base)
    if number < 0:
        floor_ceil += 1
        prefix = "-" + prefix

    remainder = number - (floor_ceil * base)
    if remainder < 0:
        remainder *= -1

    if number < base and number > -base:
        return prefix + base_chars[remainder]

    number = floor_ceil
    return _hex(number) + base_chars[remainder]


for number in range(99):
    print("{} = {}".format(number, _hex(number)))
