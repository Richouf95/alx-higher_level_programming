#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as arg
    length = len(arg) - 1
    result = 0
    for x in range(length):
        result += int(arg[x + 1])
    print("{}".format(result))
