#!/usr/bin/python3
"""
Module: function that inserts a line of text to a file,
        after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file.
    Args:
        filename (string): name of file.
        search_string (string): string to search.
        new_string (string): line to insert.
    """
    new_content = ""
    with open(filename, 'r') as file:
        for line in file:
            new_content += line
            if search_string in line:
                new_content += new_string

    with open(filename, 'w') as file:
        file.write(new_content)
