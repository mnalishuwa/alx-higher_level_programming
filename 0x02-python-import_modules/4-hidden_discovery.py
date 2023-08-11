#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    for each_name in dir(hidden_4):
        if each_name[0] == "_":
            continue
        print("{}".format(each_name))
