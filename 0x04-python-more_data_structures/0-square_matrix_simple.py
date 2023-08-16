#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        tmp = []
        for j in i:
            tmp.append(j**2)
        result.append(tmp)
    return result
