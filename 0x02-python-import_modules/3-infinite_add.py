#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as arg
    length = len(arg) - 1
    i = 1
    result = 0
    if length > 0:
        while i < len(arg):
            result += int(arg[i])
            i += 1
    print(result)
