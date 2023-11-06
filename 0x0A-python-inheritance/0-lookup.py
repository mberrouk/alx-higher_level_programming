#!/usr/bin/python3
"""
Module: function that returns the list of attributes and methods
        of an object.
"""


def lookup(obj):
    """ Return the list of available attributes and methods.
    Args:
        obj (object): the target object for attribute and method
                    inspection.
    Return:
        The list of attributes and methods.
    """
    return (dir(obj))
