#!/usr/bin/python3

"""
BaseGeometry class
"""


class BaseGeometry:
    """
    Base Geometry Class

    Methods:
        __init__
        area
    """
    def __init__(self):
        """
        Constructor method

        Args:

        Return:
            object
        """
        pass

    def area(self):
        """
        Area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator function

        Args:
            name
            value
        Return:
            None
        """
        if not isinstance(value, int) or type(value) not in (int,):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
