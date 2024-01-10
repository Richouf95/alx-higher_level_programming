#!/usr/bin/python3
"""
    Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
        append after
    """
    update = ""
    with open(filename, "r+") as fic:
        lines = fic.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
        fic.seek(0)
        fic.writelines(lines)
