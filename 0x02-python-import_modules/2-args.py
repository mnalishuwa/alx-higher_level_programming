#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    for arg_index in range(len(sys.argv)):
        if arg_index == 0:
            continue
        print("{}: {}".format(arg_index, sys.argv[arg_index]))
