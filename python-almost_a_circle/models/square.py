#!/usr/bin/python3
""" comentario """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ comentario """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.height)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.update(width=value, height=value)
