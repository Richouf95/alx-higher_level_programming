#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    listOfKey = list(a_dictionary.keys())

    for x in listOfKey:
        if value == a_dictionary.get(x):
            del a_dictionary[x]

    return a_dictionary
