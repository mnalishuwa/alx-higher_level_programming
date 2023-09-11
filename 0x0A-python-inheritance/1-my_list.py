#!/usr/bin/python3

"""
List class that inherits from list and prints sorted list
"""


class MyList(list):
    """
    My list class

    Attributes:

    Methods:

    """
    def __init__(self):
        """
        Constructor method

        Args:

        Return:
            None
        """
        super().__init__()

    def print_sorted(self):
        """
        Args:

        Return:
            None
        """
        print(sorted(self))
