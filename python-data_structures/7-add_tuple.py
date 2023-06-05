#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    valores = [0, 0]
    for i in range(len(tuple_a)):
        if i >= 2:
            break
        valores[i] += tuple_a[i]

    for i in range(len(tuple_b)):
        if i >= 2:
            break
        valores[i] += tuple_b[i]

    new_tuple = (valores[0], valores[1])
    return new_tuple
