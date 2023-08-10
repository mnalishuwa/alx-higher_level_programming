#!/usr/bin/python3
_alphabet = "abcdefghijklmnopqrstuvwxyz"
for index in range(len(_alphabet)):
    if _alphabet[index] in "eq":
        continue
    print("{}".format(_alphabet[index]), end="")
