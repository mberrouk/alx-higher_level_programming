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

    def to_json(self):
        """ Retrieve a dictionary repersentation
            of a Student
        """
        return (self.__dict__)
