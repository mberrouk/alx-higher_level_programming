#!/usr/bin/python3
"""
Module: a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """
    def __init__(self, size):
        """ initial object
        Args:
            size (int): size of the square
        """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size
