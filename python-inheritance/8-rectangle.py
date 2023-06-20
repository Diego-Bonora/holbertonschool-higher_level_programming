#!/usr/bin/python3
""" comentario """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ comentario """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._Rectangle__width = width
        self.integer_validator("height", height)
        self._Rectangle__height = height
