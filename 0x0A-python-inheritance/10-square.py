#!/usr/bin/python3


"""
Module for Square definition
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):

    """
    Square class

    Attributes:

    Methods:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size):
        """
        Constructor method

        Args:
        size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Return string representation of Rectangle instance
        """
        cls_name = self.__class__.__name__
        return str("[{}] {}/{}".format(cls_name, self.__size, self.__size))

    def area(self):
        """
        Area method

        Args:

        Return:
            int - width * height
        """
        return self.__size * self.__size
