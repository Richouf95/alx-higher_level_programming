#!/usr/bin/python3
"""
    Only sub class of
"""


def inherits_from(obj, a_class):
    """
        inherits from a class
    """
    if type(obj) != a_class:
        if issubclass(type(obj), a_class):
            return True
    return False
