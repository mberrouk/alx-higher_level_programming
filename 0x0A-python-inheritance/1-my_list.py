#!/usr/bin/python3
"""
Module: define a class 'MyList'.
"""


class MyList(list):
    """ Inherited list class """

    def print_sorted(self):
        """ Print a sorted list """
        print(sorted(self))
