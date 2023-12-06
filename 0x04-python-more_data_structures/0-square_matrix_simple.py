#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for x in matrix:
        row = []
        for y in x:
            row.append(y**2)
        result.append(row)
    return result
