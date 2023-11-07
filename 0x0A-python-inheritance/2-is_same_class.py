#!/usr/bin/python3
"""
Module: function that returns True if the object is exactly an instance
        of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """ Check if the object is an instance of the class
    Args:
        obj: object to Check
        a_class: class for Checking
    Return:
        True if the object is an instance of the class,
        otherwise alse.
    """
    return (type(obj) == a_class)
