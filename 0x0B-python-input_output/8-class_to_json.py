#!/usr/bin/python3
"""
Module: function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean) for
        JSON serialization of an object
"""


def class_to_json(obj):
    """ Return the dictionary description for
        JSON serialization of an objct.
    Args:
        obj: object
    Return:
        the dictionary description.
    """
    return (obj.__dict__)
