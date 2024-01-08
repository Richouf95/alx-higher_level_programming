#!/usr/bin/python3
"""
    Check if object is instance
"""


def is_same_class(obj, a_class):
    """
        Checker
        Args:
            obj: the object
            a_class: the class
    """
    if type(obj) == a_class:
        return True
    return False
