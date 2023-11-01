#!/usr/bin/python3
# 101-locked_class.py
"""
Module: define a class that prevents the usr from dynamically
creating new instance attribute.
"""


class LockedClass:
    """ Class with no object attribute, that prevents the
    usr from dynamically creating new instance attribute.
    except if the new instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
