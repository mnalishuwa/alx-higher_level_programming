#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# YOUR CODE HERE
floor_ceil = number // 10

# python uses the floor when it performs int division
# therefore using modulo(%) can lead to undesired
# results for negative numbers, because it uses
# floor in calculating modulo in order for math ops
# to remain consistent.

# Therefore, we need to use the ceiling in calculating
# the remainder when the number is negative
if number < 0:
    floor_ceil += 1  # result is ceiling if n < 0
rmd = number - (floor_ceil * 10)

if rmd == 0:
    print(f"Last digit of {number:d} is {rmd:d} and is 0")
elif rmd > 5:
    print(f"Last digit of {number:d} is {rmd:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {rmd:d} and is less than 6 and not 0")
