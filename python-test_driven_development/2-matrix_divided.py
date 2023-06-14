#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    else:
        for i in range(len(matrix)):
            equal_len = len(matrix[i])
            if not isinstance(matrix[i], list):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        for i in matrix:
            for x in i:
                if not isinstance(x, int) and not isinstance(x, float):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
        for i in matrix:
            if len(i) != equal_len:
                raise TypeError(
                    "Each row of the matrix must have the same size")
    if div == None:
        return matrix
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        list_append = []
        for x in range(len(matrix[i])):
            list_append.append(round(matrix[i][x] / div, 2))
        new_matrix.append(list_append)
    return new_matrix
