#!/bin/usr/python3


def no_c(my_string):
    a = [x for x in my_string if x not in 'Cc']
    s = ''.join(a)
    return (s)
