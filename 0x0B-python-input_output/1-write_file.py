#!/usr/bin/python3
"""
    Write to a file
"""


def write_file(filename="", text=""):
    """
        Write a string into a file
    """
    i = 0
    for c in text:
        i += 1

    with open(filename, "w") as fic:
        fic.write(text)
    return i
