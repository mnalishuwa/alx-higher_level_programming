#!/usr/bin/python3

"""Square module Docs"""


class Square:
    """
    Square Class Base Template v0.2 - size validation

    Attributes:
        size (int): +ve square side
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Contructor method, init instance variables
        Args:
            size: int
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get size method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Get size method

        Args:
            value: int
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get position method
        """
        return self.__position

    @position.setter
    def position(self, value: tuple[int, int] = (0, 0)) -> None:
        """
        Set square postion
        Args:
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        get area method
        """
        return self.size * self.size

    def my_print(self):
        """
        Prints a square
        """
        if self.size == 0:
            print()
            return
        for length in range(self.size):
            print(self.position[0] * " ", end="")
            for width in range(self.size):
                print("#", end="")
            print()
