#!/usr/bin/python3
"""
Module: function that prints a square with the character '#'
"""


def print_square(size):
    """ Print a square on stdout
    Args:
        size (int): The size length of the square.
    Raises:
        - TypeError if size is not an integer,
        or if size is a float and is less than 0.
        - ValueError if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    row = "#" * size
    for line in range(size):
        print(row)
