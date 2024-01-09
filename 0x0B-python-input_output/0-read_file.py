#!/usr/bin/python3
"""
    Read file
"""


def read_file(filename=""):
    """
        Read and print file content
    """
    with open(filename, "r") as fic:
        content = fic.read()
        print(content, end="")
