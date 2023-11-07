#!/usr/bin/python3
"""
Module: function that writes an Object to a text file,
        using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """ write an object to a text file (JSON representation).
    Args:
        my_obj: object.
        filename: name of file.
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
