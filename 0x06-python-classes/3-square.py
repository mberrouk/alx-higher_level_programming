#!/usr/bin/python3
"""Write Square"""


class Square:
    """ Square class defines a square """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ returns the current square area """
    def area(self):
        return (self.__size ** 2)
