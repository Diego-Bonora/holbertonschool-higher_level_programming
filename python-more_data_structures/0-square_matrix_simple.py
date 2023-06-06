#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        inner_matrix = []
        for x in i:
            inner_matrix.append(x**2)
        new_matrix.append(inner_matrix)
    return new_matrix
