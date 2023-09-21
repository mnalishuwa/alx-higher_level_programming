#!/usr/bin/python3


"""
Base module docs
"""


import json


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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Arguments:
            dictionary(dict) - keyword arguments (kwargs)

        Return:
            object(Rectangle, Square)
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            obj = cls(1, 0, 0)
        else:
            return cls()
        obj.update(**dictionary)
        return obj

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation

        Arguments:
            json_string(string) - JSON string representation

        Return:
            list
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Reads from file and creates a list
        of instances from the json string
        in file. Returns list of instances

        Arguments:

        Return:
            list - list of Base subclasses
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as file_handle:
                json_text_data = file_handle.read()
                list_dictionaries = cls.from_json_string(json_text_data)
                return [cls.create(**obj_dict)
                        for obj_dict in list_dictionaries]
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs
        to a file

        Arguments:
            list_obj(list) - list of Rectangle or Square objects

        Attributes:
            filename(string) - filename
            list_dictionaries(list) - list with dict objects

        Return:
            None
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w+", encoding="utf-8") as file_handle:
            file_handle.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return JSON representation of list_dictionaries

        Args:
            list_dictionaries - list object

        Return:
            json object
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
