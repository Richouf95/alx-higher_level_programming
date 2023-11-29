#!/usr/bin/python3
def print_last_digit(number):
    n = number - (int(number / 10) * 10)
    if n < 0:
        n = n * -1
    print("{}".format(n), end="")
    return n
