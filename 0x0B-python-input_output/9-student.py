#!/usr/bin/python3
"""
    Student to JSON
"""


class Student:
    """
        Student Class
    """
    def __init__(self, fn, ln, a):
        """
            Initilizing
        """
        self.first_name = fn
        self.last_name = ln
        self.age = a

    def to_json(self):
        """
            parse this class to json
        """
        return self.__dict__
