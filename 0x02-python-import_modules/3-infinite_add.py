#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    result = 0
    for arg_index in range(1, len(sys.argv)):
        result += int(sys.argv[arg_index])
    print(result)
