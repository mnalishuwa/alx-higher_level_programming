#!/usr/bin/python3

"""
Rectangle class definition
"""


class Rectangle:
    """
    Rectangle blueprint

    Attributes:
        number_of_instances(int)
        print_symbol

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
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Detect deletion
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """
        Return string representation of Rectangle instance
        """
        rows = self.height
        cols = self.width
        symbol = str(self.print_symbol)
        str_rectangle = ""
        for row in range(rows):
            for col in range(cols):
                str_rectangle += symbol
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        creates a new instance
        """
        return cls(size, size)

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
