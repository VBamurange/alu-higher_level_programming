#!/usr/bin/python3
"""divide a matrix"""


def matrix_divided(matrix, div):
    """matrix function"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for v in matrix:
        if type(v) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(v)
        elif size != len(v):
            raise TypeError("Each row of the matrix must have the same size")
        for w in v:
            if type(w) is not int and type(w) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(w / div, 2) for w in v] for v in matrix]
