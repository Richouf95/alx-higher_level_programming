#!/usr/bin/python3
count = 122
while count > 96:
    currentChr = count
    if currentChr % 2:
        currentChr -= 32
    print("{}".format(chr(currentChr)), end = '')
    count -= 1
