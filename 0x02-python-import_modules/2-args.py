#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 0:
        print("0 arguments.")
    elif len(sys.argv) == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv)))

    for arg_index in len(sys.argv):
        print("{}: {}".format(arg_index + 1, sys.argv[arg_index]))
