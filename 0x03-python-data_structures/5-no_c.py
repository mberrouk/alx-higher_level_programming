#!/bin/usr/python3


def no_c(my_string):
    a = [x for x in my_string if x != 'c' and x != 'C']
    s = ''.join(a)
    return (s)
