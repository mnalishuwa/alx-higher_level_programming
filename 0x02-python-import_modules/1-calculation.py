#!/usr/bin/python3

import calculator_1 as calc

a = 10
b = 5

# print("{} + {} = {}".format(a, b, calc.add(a, b)))
print(f"{a:d} + {b:d} = {calc.add(a, b):d}")
print(f"{a:d} - {b:d} = {calc.sub(a, b):d}")
print(f"{a:d} * {b:d} = {calc.mul(a, b):d}")
print(f"{a:d} / {b:d} = {calc.div(a, b):d}")
