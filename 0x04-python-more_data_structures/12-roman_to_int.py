#!/usr/bin/python3


def roman_to_int(roman_string):

    chart = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100,
             'D': 500, 'M': 1000,'E': 0}
    result = 0
    if (not roman_string) or (type(roman_string) != str):
        return result
    roman_string = roman_string.upper()
    roman_string += 'E'
    size = len(roman_string)
    num = chart[roman_string[0]]
    for idx in range(1, size):
        if chart[roman_string[idx]] >  num:
            result += chart[roman_string[idx]] - num
            idx += 1
        else:
            result += num
        num = chart[roman_string[idx]]
    return result
