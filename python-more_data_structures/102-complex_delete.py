#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for key, val in a_dictionary.items():
        if val == value:
            keys.append(key)
    for i in keys:
        a_dictionary.pop(i)
    return a_dictionary
