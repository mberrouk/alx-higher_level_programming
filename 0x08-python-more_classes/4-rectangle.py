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
        self.__height = height
        self.__width = width

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

    def area(self):
        """ rectangle area """
        return (self.__height * self.width)

    def perimeter(self):
        """ rectangle perimeter """
        if not self.__height or not self.width:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ print the rectangle """
        if not self.__height or not self.__width:
            return ("")
        string = ""
        for x in range(self.__height):
            for y in range(self.__width):
                string += '#'
            if x < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")
