#!/usr/bin/python3
""" comentario """


class Base():
    """ comentario """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
