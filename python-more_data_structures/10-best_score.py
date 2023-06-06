#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        for i in sorted(a_dictionary.values()):
            value = i
        for key, val in a_dictionary.items():
            if value == val:
                return key
    return value
