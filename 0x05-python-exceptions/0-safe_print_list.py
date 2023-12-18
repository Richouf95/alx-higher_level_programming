#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    length = 0

    try:
        for i in my_list:
            if length < x:
                print(i, end="")
                length += 1
        print("")
    except IndexError:
        pass

    return length
