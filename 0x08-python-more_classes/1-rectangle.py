#!/usr/bin/python3
"""
    ``1-rectangle.py``: A Python File Defining a Rectangle Class.
"""


class Rectangle:
    """ class Rectangle defines a rectangle."""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Private instance attribute to retrieve width"""
        return (self.width)

    @width.setter
    def width(self, value):
        """ Setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Private instance attribute to retrieve height"""
        return (self.height)

    @height.setter
    def height(self, value):
        """ Setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
