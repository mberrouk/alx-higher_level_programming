#!/usr/bin/python3
# 2-matrix_divided.py
"""Funcion divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix: A lists of ints or floats.
        div: divisor.
    Return:
        matrix of the result of the division.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if ((not isinstance(matrix, list) or not matrix) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(err_msg)
    if not all((isinstance(num, int) or isinstance(num, float))
               for num in [x for row in matrix for x in row]):
        raise TypeError(err_msg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(x / div, 2) for x in row] for row in matrix]
