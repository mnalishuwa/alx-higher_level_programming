#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import calculator_1 as calc

    num_args = len(argv)
    funcs = [calc.add, calc.sub, calc.mul, calc.div]
    ops = "+-*/"

    if (num_args - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not (argv[2] in ops):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    for op_index in range(len(ops)):
        if argv[2] == ops[op_index]:
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3],
                                         funcs[op_index](int(argv[1]),
                                                         int(argv[3]))))
            exit(0)
