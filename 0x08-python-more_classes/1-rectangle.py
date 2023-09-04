#!/usr/bin/python3
""" Rectangle class defines a rectangle """


class Rectangle:
    """ The rectangle class """

    def __init__(self, width=0, height=0):
        """ Initializing class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: value is not an integer
            ValueError: value is less than zero
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrives height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
