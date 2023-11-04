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

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
