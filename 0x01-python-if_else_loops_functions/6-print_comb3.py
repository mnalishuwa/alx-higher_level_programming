#!/usr/bin/python3

for x in range(10):
    for y in range(x + 1, 10):
        if (x + y) < (9 + 8):
            print(x, y, sep="", end=", ")
            continue
        print("{}{}".format(x, y))
