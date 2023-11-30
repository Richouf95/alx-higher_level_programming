#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as arg
    i = 1
    length = len(arg) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))

    while i <= length:
        print("{}: {}".format(i, arg[i]))
        i += 1
