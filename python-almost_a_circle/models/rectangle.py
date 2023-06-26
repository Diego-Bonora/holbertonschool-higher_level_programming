#!/usr/bin/python3
""" comentario """
from models.base import Base


class Rectangle(Base):
    """ comentario """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__widht = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def widht(self):
        return self.__widht

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @widht.setter
    def widht(self, value):
        self.__widht = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__x = value
