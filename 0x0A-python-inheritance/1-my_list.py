#!/usr/bin/python3
"""
    My list
"""


class MyList(list):
    """
        sort and print a list
    """
    def print_sorted(self):
        """
            Sort a list
        """
        print(sorted(self))
