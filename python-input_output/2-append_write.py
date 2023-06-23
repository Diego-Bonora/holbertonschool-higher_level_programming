#!/usr/bin/python3
""" comentario """


def append_write(filename="", text=""):
    """ comentario """
    with open(filename, encoding="utf-8", mode="a") as f:
        return f.write(text)
