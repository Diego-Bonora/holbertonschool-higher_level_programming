#!/usr/bin/python3
""" comentario """


def save_to_json_file(my_obj, filename):
    """ comentario """
    import json
    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(json.dumps(my_obj))
