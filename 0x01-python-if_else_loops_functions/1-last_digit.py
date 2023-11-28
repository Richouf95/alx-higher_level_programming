#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number - (int(number / 10) * 10)
if n > 5:
    print("Last digit of", number, "is", n, "and is greater than 5")
if digit < 6:
    if digit == 0:
        print("Last digit of", number, "is", n, "and is 0")
    else:
        print("Last digit of", number, "is", n, "and is less than 6 and not 0")
