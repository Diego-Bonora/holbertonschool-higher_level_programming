#!/usr/bin/python3
text1 = "{}, "
text2 = "{}"
for i in range(100):
    if i != 99:
        print(text1.format(str(i).zfill(2)), end="")
    else:
        print(text2.format(str(i).zfill(2)))
