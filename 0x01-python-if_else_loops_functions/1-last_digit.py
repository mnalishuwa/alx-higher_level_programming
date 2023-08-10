#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rmd = number % 10
if number < 0:
    rmd *= -1
# YOUR CODE HERE
if rmd == 0:
    print(f"Last digit of {number:d} is {rmd:d} and is 0")
elif rmd > 5:
    print(f"Last digit of {number:d} is {rmd:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {rmd:d} and is less than 6 and not 0")
