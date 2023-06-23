#!/usr/bin/python3
""" comentario """


def load_from_json_file(filename):
    """ comentario """
    import json
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
