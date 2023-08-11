#!/usr/bin/python3

for each_number in range(100):
    if (each_number < 99):
        print("{:02d}, ".format(each_number), end="")
        continue
    print("{:02d}".format(each_number))
