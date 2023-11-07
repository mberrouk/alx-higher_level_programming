#!/usr/bin/python3
"""
Module: function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of text file.
    Args:
        filename (string): text file to open.
        text (string): content.
    """
    with open(filename, "a") as file:
        file.write(text)
    return (len(text))
