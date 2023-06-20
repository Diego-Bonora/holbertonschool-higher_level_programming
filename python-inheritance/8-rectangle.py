#!/usr/bin/python3
""" comentario """


class BaseGeometry():
    """ comentario """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" comentario """


class Rectangle(BaseGeometry):
    """ comentario """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._Rectangle__width = width
        self.integer_validator("height", height)
        self._Rectangle__height = height
