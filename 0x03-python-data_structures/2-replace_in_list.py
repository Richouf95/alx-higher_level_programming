#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)

    if idx < 0:
        return my_list
    elif idx > length - 1:
        return my_list
    else:
        newList = my_list
        newList[idx] = element
        return newList
