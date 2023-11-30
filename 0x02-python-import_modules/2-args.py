#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as arg
    i = 1
    length = len(arg)
    if length == 1:
        print("0 : arguments")
    if length == 2:
        print("{} : arguments".format(length - 1))
        while i < length:
            print("{}: {}".format(i, arg[i]))
            i += 1
    if length > 2:
        print("{} : arguments".format(length - 1))
        while i < length:
            print("{}: {}".format(i, arg[i]))
            i += 1
