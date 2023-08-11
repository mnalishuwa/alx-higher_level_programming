#!/usr/bin/python3


def print_last_digit(number):

    divisor = 10
    if number < 0:
        divisor *= -1

    remainder = number - ((number // divisor) * divisor)
    if remainder < 0:
        remainder *= -1
    print(remainder, end="")
    return remainder
