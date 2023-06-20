#!/usr/bin/python3
""" comentario """


class MyList(list):
    """ comentario """

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
