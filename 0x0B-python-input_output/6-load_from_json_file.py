#!/usr/bin/python3
"""
    Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
        load json from file
    """
    with open(filename, "r") as fic:
        return json.load(fic)
