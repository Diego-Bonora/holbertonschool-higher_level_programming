#!/usr/bin/python3
""" comentario """


def inherits_from(obj, a_class):
    """ comentario """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    else:
        return False
