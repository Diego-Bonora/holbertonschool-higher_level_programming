#!/usr/bin/python3
""" comentario """


def say_my_name(first_name, last_name=""):
    """ comentario """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
