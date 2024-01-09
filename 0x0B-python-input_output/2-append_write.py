#!/usr/bin/python3
"""
    Write to a file
"""


def append_write(filename="", text=""):
    """
        Write a string at the end of  a file
    """
    with open(filename, "a") as fic:
        return fic.write(text)
