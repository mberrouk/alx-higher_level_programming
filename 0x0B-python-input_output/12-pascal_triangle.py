#!/usr/bin/python3
"""
Module: returns a list of lists of integers representing
        the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """ Return a list of lists of integers representing
        the Pascal's triangle.
    Arsg:
        n (integer): size of triangle.
    """
    tmp = []

    if n <= 0:
        return (tmp)
    triangle = [[1]]
    while (len(triangle) < n):
        tmp = [1]
        tmp_triangle = triangle[-1]
        for i in range(len(tmp_triangle) - 1):
            tmp.append(tmp_triangle[i] + tmp_triangle[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
