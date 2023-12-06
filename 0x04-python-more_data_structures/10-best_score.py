#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    best = 0
    theBest = ""

    for x in a_dictionary:
        item = a_dictionary[x]
        if item > best:
            best = item
            theBest = x
    return theBest
