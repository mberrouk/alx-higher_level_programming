#!/usr/bin/python3
"""
Module: function return a string "BestSchool".
"""


def magic_string():
    """ function that returns a string n times. """
    magic_string.n = getattr(magic_string, "n", 0) + 1
    return (("BestSchool, " * (magic_string.n - 1)) + "BestSchool")
