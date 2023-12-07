#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    divider = 0

    if len(my_list) == 0:
        return 0

    for x in my_list:
        mul = x[0] * x[1]
        total += mul
        divider += x[1]

    return total / divider
