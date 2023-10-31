#!/usr/bin/python3
"""
    ``1-rectangle.py``: A Python File Defining a Rectangle Class.
"""


class Rectangle:
    """ class Rectangle defines a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Private instance attribute to retrieve width"""
        return (self.__width)

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
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the rectangle area """
        return (self.height * self.width)

    def perimeter(self):
        """ Return he rectangle perimeter """
        if not self.width or not self.height:
            return (0)
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """ Return a string of the rectangle with the character #.
        """
        if not self.height or not self.width:
            return ("")
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """ Return a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @@staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the Rectangle with the greater area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
