#!/usr/bin/python3
""" Rectangle class defines a rectangle """


class Rectangle:
    """ The rectangle class """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                try:
                    string += str(self.print_symbol)
                except Exception:
                    string += type(self).print_symbol
            if x < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ prints a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
