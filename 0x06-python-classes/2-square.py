#!/usr/bin/python3

"""Square module Docs"""


class Square:
    """
    Square Class Base Template v0.2 - size validation

    Attributes:
        size (int): +ve square side
    """
    def __init__(self, size=0):
        """
        Contructor method, init instance variables
        Args:
            size: int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
