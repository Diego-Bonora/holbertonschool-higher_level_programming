#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    not_usable = []
    for i in my_list:
        if i not in not_usable:
            add += i
            not_usable.append(i)
    return add
