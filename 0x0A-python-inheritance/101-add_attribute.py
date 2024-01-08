#!usr/bin/python3
"""
    Can I
"""


def add_attribute(obj, attribute, value):
    """
        Add attribute if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
