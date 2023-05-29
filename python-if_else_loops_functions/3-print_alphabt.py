#!/usr/bin/python3
text = "{}"
for i in range(97, 123):
    if chr(i) != "p" and chr(i) != "e":
        print(text.format(chr(i)), end="")
