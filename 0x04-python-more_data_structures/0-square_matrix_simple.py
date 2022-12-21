#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        res = list(map(lambda x: x ** 2, i))
        new_matrix.append(res)
    return new_matrix
