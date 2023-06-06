#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        roman_leters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        add = 0
        sub = 0
        big = 0
        r_s = roman_string[::-1]
        for i in range(len(r_s)):
            if r_s[i] == 0 and r_s[i] in roman_leters:
                add += roman_leters[r_s[i]]
                big = roman_leters[r_s[i]]
            elif r_s[i] in roman_leters and roman_leters[r_s[i]] < big:
                sub += roman_leters[r_s[i]]
            elif r_s[i] in roman_leters:
                add += roman_leters[r_s[i]]
                add -= sub
                sub = 0
                big = roman_leters[r_s[i]]
        add -= sub
        return add
    else:
        return 0
