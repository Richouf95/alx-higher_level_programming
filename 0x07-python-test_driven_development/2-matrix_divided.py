#!/usr/bin/python3
"""
    divide a matrix elements
"""


def matrix_divided(matrix, div):
    """
        This function dive each matrix element
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for x in matrix:
        r = []
        for y in x:
            r.append(round(y / div, 2))
        result.append(r)

    return result
