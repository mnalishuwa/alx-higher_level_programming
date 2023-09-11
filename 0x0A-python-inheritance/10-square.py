#!/usr/bin/python3

"""
Square class
"""


BaseGeometry = __import__('9-rectangle.py').BaseGeometry


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

    def __str__(self):
        """
        Return string representation of Rectangle instance
        """
        cls_name = self.__class__.__bases__[0].__name__
        return str("[{}] {}/{}".format(cls_name, self.__size, self.__size))
