#!/usr/bin/python3
""" comentario """


def write_file(filename="", text=""):
    """ comentario """
    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(text)
