#!/usr/bin/python3

"""
Rectangle class definition
"""


class Rectangle:
    """
    Rectangle blueprint

    Attributes:

    Methods:
        __init__(self, width, height)
        height(self)
        height(self, value)
        width(self)
        width(self, value)
    """
    def __init__(self, width=0, height=0):
        """
        Rectangle constructor method

        Arguments:
            __width(int):
            __height(int):

        Attributes:
            __width(int):
            __height(int):
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        get height method

        Return:
            int, height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set length method

        Arguments:
            value(int)

        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        get width method

        Return:
            int, width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width method

        Arguments:
            value(int)

        Return:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
