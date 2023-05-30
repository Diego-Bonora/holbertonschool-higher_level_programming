#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        orden = ord(str[i])
        if orden > 96 and orden < 123:
            orden = orden - 32
        print("{}".format(chr(orden)), end="")
    print()