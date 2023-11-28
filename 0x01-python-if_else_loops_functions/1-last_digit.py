#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberInString = str(number)
lastPos = len(numberInString) - 1
lastItem = int(numberInString[lastPos])
if numberInString[0] == '-':
    lastItem = lastItem * -1

if lastItem > 5:
    print("Last digit of", number, "is", lastItem, "and is greater than 5")
elif lastItem == 0:
    print("Last digit of", number, "is", lastItem, "and is 0")
elif lastItem < 6 and not 0:
    print("Last digit of", number, "is", lastItem, "and is less than 6 and not 0")
