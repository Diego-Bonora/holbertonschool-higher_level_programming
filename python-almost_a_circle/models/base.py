#!/usr/bin/python3
""" comentario """
import json


class Base():
    """ comentario """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a list of dicts to a json file """
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []

        dict_list = []
        for i in list_objs:
            dict_list.append(i.to_dictionary())

        with open(str(filename), encoding="utf-8", mode="w+") as f:
            f.write(cls.to_json_string(dict_list))
