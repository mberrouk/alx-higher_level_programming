#!/usr/bin/python3
"""Write Square"""


class Square:
    """ Square class defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
        self.size = value

    @property
    def position(self):
        """ return position """
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        var1, var2 = value
        if var1 < 0 or var2 < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square """
        if self.size == 0:
            print("")
            return
        for k in range(self.position[1]):
            print("")
        for i in range(self.size):
            for pp in range(self.position[0]):
                print(end=" ")
            for j in range(self.size):
                print("#", end="")
            print("")
