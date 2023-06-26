#!/usr/bin/python3
""" comentario """
from models.base import Base


class Rectangle(Base):
    """ comentario """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.widht = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def widht(self):
        return self.__widht

    @widht.setter
    def widht(self, value):
        self.__widht = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__x = value
