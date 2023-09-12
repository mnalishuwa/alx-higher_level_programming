#!/usr/bin/python3

"""
10-square module docs

Square class inherits from Rectangle class

Rectangle class inherits from BaseGeometry
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    Square class base blueprint

    Attributes:
    size (int) - +ve square side

    Methods:
    __init__(self, size)
    __str__(self)
    """
    def __init__(self, size):
        """
        Constructor method

        Args:
            size (int): +ve square side

        Attributes:
            __size(int):

        Return:
            object
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
