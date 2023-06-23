#!/usr/bin/python3
""" comentario """


def pascal_triangle(n):
    """ comentario """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        matrix = [[1], [1, 1]]
        for i in range(1, n - 1):
            list = matrix[i].copy()
            for x in range(1, len(list)):
                list[x] = list[x] + matrix[i][x - 1]
            list.append(1)
            matrix.append(list)
        return matrix
