#!/usr/bin/python3
"""
Module: define class Student that defines a student.
"""


class Student:
    """ class define a student """
    def __init__(self, first_name, last_name, age):
        """ initial object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieve a dictionary repersentation
            of a Student
        """
        if (attrs and type(attrs) == list
                and all(type(arg) == str for arg in attrs)):
            new_dict = {key: self.__dict__[key]
                        for key in attrs if key in self.__dict__}
            return (new_dict)
        return (self.__dict__)
