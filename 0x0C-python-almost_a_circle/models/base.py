#!/usr/bin/python3
"""
Module: models/base.py - Definition of the Base class.

This module contains the implementation of the Base class,
which serves as the foundation for other classes in the models package.

Classes:
    - Base: The base class with a private class attribute and a constructor.

Usage:
    To use this module, import the Base class and create instances of it.

Example:
    from models.base import Base

    # Creating an instance of Base with automatic ID assignment
    obj1 = Base()
    print(obj1.id)  # Output: 1

    # Creating an instance of Base with a specific ID
    obj2 = Base(100)
    print(obj2.id)  # Output: 100
"""
import json


class Base:
    """ First class.

    Attributes:
        id (int): Public instance attribute representing the object's ID.

    Class Attributes:
        __nb_objects (int): Private class attribute to track
        the number of objects created.

    Methods:
        __init__(self, id=None): Class constructor to initialize
        the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor for Base.

        Args:
            id (int, optional): If provided, assigns the specified ID to
            the object.cIf not provided, increments __nb_objects and assigns
            the new value to the object's ID.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            strs = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(strs)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """List of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                list_dicts = Base.from_json_string(file.read())
            return [cls.create(**inst) for inst in list_dicts]
        except IOError:
            return []
