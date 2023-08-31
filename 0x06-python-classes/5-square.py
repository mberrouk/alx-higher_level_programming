#!/usr/bin/python3
"""Write Square"""


class Square:
    """ Square class defines a square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ return size of square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ set the size of square """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square """
        if self.size is 0:
            print("")
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
