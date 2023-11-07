#!/usr/bin/python3
"""
Module: function that returns the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """ Return the JSON representation of an object.
    Args:
        my_obj: an object.
    """
    return (json.dumps(my_obj))
