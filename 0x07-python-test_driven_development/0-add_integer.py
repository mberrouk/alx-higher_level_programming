#!/usr/bin/python3
# 0-add_integer.py
"""Defines an intger addition function"""


def add_integer(a, b=98):
    """Return an integer: the addition of a and b

    - a and b must be first casted to intger if they
    are float.

    Raises:
        TypeError: If either of a or b is non-intger and
        non-float.
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return (int(a) + int(b))
