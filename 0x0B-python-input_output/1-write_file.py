#!/usr/bin/python3
"""
Module: Write a function that writes a string to a text file
    (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """ Write a string to a text file.
    Args:
        filename (string): name of file.
        text (string): content to write.
    """
    with open(filename, "w") as file:
        file.write(text)
