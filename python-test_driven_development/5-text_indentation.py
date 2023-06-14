#!/usr/bin/python3
""" comentario """


def text_indentation(text):
    """ comentario """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    jump = [".", "?", ":"]
    for i in range(len(text)):
        if text[i] in jump:
            print(text[i])
            print()
        elif text[i] == " " and text[i - 1] in jump:
            continue
        else:
            print(text[i], end="")
