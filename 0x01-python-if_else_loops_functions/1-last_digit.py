#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if (number % 10) > 5:
    print(f"Last digit of {number:d} is and is greater than 5\n")
elif (number % 10 < 6):
    print(f"Last digit of {number:d} is 
