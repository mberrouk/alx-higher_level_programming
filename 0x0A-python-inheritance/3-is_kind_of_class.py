#!/usr/bin/python3
"""
Module: function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ Check if the obj is an insatnce of or if the object is an
    instance of a class that inherited from the class.
    Return:
        True or False.
    """
    return (isinstance(obj, a_class))
