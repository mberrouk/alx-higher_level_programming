#!/usr/bin/python3
"""
Module: unction that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """ Read a text file and print it to stdout.
    Args:
        filename (string): file to read.
    """
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
