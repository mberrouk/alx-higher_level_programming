#!/usr/bin/python3
"""
Module: function that prints a text with 2 new line.
"""


def text_indentation(text):
    """ Print a text with 2 new lines after each of: '.', '?' and ':'.
    Args:
        text (str): text must be a string
    Raises:
        - TypeError if text not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:" or text[i] == '\n':
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                    i += 1
            continue
        i += 1
