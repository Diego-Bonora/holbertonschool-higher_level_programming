#!/usr/bin/python3
"""
add_integer - function for adding 2 int numbers
a: first input number
b: second input number
"""


def add_integer(a, b=98):
    """
    first checks if a and b are floats or int, then returns the int add
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
