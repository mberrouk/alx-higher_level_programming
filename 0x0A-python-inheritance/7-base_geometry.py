#!/usr/bin/python3
"""
Module: define a BaseGeometry class with a public method.
"""


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value.
        Args:
            name: is always a string.
            value: value to Validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
