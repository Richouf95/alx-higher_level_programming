#!/usr/bin/python3
"""
    Class to JSON
"""


def class_to_json(obj):
    """
        parse class to json
    """
    return obj.__dict__
