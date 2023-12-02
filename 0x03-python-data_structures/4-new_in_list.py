#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)

    if idx < 0:
        return my_list
    elif idx > length - 1:
        return my_list
    else:
        newList = my_list.copy()
        newList[idx] = element
        return newList
