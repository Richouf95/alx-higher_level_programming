#!/usr/bin/python3
"""
    add two number
"""


def add_integer(a, b=98):
    """
        Function add
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")

    A = int(a)
    B = int(b)

    return A + B
