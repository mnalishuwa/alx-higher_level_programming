#!/usr/bin/python3


"""
Peak finding solution file
"""


def find_peak(list_of_integers):
    """
    Function to find peak in a list of ints
    """
    high = size = len(list_of_integers)
    low = 0

    while low < high:
        mid = (low + high) // 2
        left = float('-inf') if mid <= 0 else list_of_integers[mid - 1]
        right = float('-inf') if mid >= size - 1 else list_of_integers[mid + 1]
        if list_of_integers[mid] >= left and list_of_integers[mid] >= right:
            return list_of_integers[mid]
        elif list_of_integers[mid] < left:
            high = mid
        else:
            low = mid
    return None
