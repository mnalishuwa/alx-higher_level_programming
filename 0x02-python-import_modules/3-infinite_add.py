#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    result = 0
    for each_arg in sys.argv:
        result += int(each_arg)
    print(result)
