#!/usr/bin/python3
t_f = True
for i in range(122, 96, -1):
    if t_f:
        print("{}".format(chr(i)), end="")
        t_f = False
    else:
        print("{}".format(chr(i - 32)), end="")
        t_f = True
