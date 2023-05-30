#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 64 and ord(str[i]) < 91:
            for_printing = str[i]
        elif ord(str[i]) > 96 and ord(str[i]) < 123:
            for_printing = chr(ord(str[i]) - 32)
        else:
            for_printing = str[i]
        print("{0}".format(for_printing), end="")
    print("")
