#!/usr/bin/python3
""" comentario """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ comentario """

    def __init__(self, size):
        self.integer_validator("size", size)
        self._Square__size = size

    def area(self):
        return self._Square__size ** 2

    def __str__(self):
        return "[Square] {0}/{0}".format(self._Square__size)
