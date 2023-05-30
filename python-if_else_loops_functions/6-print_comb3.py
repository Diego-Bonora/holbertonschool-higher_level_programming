#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j == 0 and i == 0:
            print("{0}".format(str(i) + str(j)), end="")
        elif i != j and j > i:
            print(", {0}".format(str(i) + str(j)), end="")
print("")
