#!/usr/bin/python3
""" comentario """


class Student():
    """ comentario """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict.update({i: self.__dict__[i]})
            return new_dict
        else:
            return self.__dict__
