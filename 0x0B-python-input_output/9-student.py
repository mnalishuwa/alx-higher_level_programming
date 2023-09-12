#!/usr/bin/python3

"""
Module 9-student docs

Class Student defines student object data structure
"""


class Student:
    """
    Data structure for student data

    Attributes:
        first_name - str
        last_name - str
        age - int, student age

    Methods:
        __init__(self, first_name, last_name, age)
        to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor method

        Args:
            first_name
            last_name
            age

        Return:
            object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return dictionary representation of student

        Args:

        Return:
            dict
        """
        return self.__dict__
