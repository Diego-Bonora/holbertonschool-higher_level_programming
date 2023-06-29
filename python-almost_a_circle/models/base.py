#!/usr/bin/python3
""" comentario """
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """ returns a list of dictionaries from a json file """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ function to create a new object """
        if cls.__name__ == "Rectangle":
            new_dummy = cls(1, 1)
        else:
            new_dummy = cls(1)
        new_dummy.update(**dictionary)
        return new_dummy

    @classmethod
    def load_from_file(cls):
        """ function that returns a list of new objects from a json file """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, encoding="utf-8", mode="r") as f:
                dict_list = cls.from_json_string(f.read())
                class_list = []
                for i in dict_list:
                    class_list.append(cls.create())
                return class_list
        else:
            return []
