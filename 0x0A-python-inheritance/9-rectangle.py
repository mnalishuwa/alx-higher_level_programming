#!/usr/bin/python3

"""
Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Constructor method

        Args:
            width
            height
        Return:
            object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Area method

        Args:

        Return:
            int - width * height
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of Rectangle instance
        """
        cls_name = self.__class__.__name__
        return str("[{}] {}/{}".format(cls_name, self.__width, self.__height))
