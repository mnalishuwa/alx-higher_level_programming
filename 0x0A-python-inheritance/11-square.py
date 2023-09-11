#!/usr/bin/python3

"""
Square class
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    square class

    Attributes:

    Methods:
        __init__
        area
    """
    def __init__(self, size):
        """
        Constructor method
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
