#!/usr/bin/python3
"""
Module: function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """ create an Object from a “JSON file”.
    Args:
        filename (string): name of file.
    """
    with open(filename, "r") as file:
        return (json.load(file))
