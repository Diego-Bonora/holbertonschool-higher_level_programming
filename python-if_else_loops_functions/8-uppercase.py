#!/usr/bin/python3
def uppercase(str):
    text = "{}"
    text_null = ""
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            for_printing = chr(ord(str[i]) - 32)
        else:
            for_printing = str[i]
        print(text.format(for_printing), end="")
    print(text_null)
