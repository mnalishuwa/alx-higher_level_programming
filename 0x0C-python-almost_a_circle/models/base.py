#!/usr/bin/python3


"""
Base module docs
"""


class Base:
    """
    Base class template

    Attributes:
        __nb_objects - number of objects/instances

    Methods:
        __init__(self, id) - constructor method
    """
    __nb_objects = 1

    def __init__(self, id=None):
        """
        Base constructor method

        Arguments:
            id

        Attributes:
            id

        Return:
            object
        """
        self.id = self.__class__.__nb_objects
        if id is not None:
            self.id = id
            return
        self.__class__.__nb_objects += 1
