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
        __del__(self)
        __str__(self)
        __repr__(self)
        height(self)
        height(self, value)
        width(self)
        width(self, value)
        area(self)
        perimiter(self)
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

    def __del__(self):
        """
        Detect deletion
        """
        print("Bye rectangle...")

    def __str__(self):
        """
        Return string representation of Rectangle instance
        """
        rows = self.height
        cols = self.width
        str_rectangle = ""
        for row in range(rows):
            for col in range(cols):
                str_rectangle += "#"
            if row != rows - 1 and cols != 0:
                str_rectangle += "\n"
        return str_rectangle

    def __repr__(self):
        """
        Return printable representation of object
        """
        cls_name = self.__class__.__name__
        return "{}({}, {})".format(cls_name, self.width, self.height)

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

    def area(self):
        """
        calculates area of rectangle instance

        Return:
            int, area = width x height
        """
        return self.width * self.height

    def perimeter(self):
        """
        calculates perimeter of rectangle instance

        Return:
            int, perimeter = (width + height) x 2
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
