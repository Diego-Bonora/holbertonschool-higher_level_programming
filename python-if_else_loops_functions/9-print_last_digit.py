#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number
    if last_digit < 0:
        last_digit = last_digit * -1
    print("{}".format(last_digit % 10), end="")
    return last_digit % 10
