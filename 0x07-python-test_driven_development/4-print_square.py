#!/usr/bin/python3
"""
    Print square
"""


def print_square(size):
    """
        This function print a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="" if y < size -1 else "\n")
