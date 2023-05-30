#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if j == 1 and i == 0:
            print("{0}".format(str(i) + str(j)), end="")
        elif i != j and j > i:
            print(", {0}".format(str(i) + str(j)), end="")
print("")
