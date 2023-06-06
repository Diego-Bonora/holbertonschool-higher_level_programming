#!/usr/bin/python
def roman_to_int(roman_string):
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    add = 0
    sub = 0
    for i in roman_string:
        if i == "I":
            sub += 1
        elif i in roman_numbers:
            add += roman_numbers[i]
            add -= sub
            sub = 0
    add += sub
    return add
