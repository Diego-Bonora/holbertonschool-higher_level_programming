#!/usr/bin/python3
""" comentario """


def print_square(size):
    """ comentario """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        for x in range(size):
            print("#", end="")
        print()
