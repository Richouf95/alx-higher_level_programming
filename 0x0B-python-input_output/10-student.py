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

    def to_json(self, attrs=None):
        """
            parse this class to json
        """
        if type(attrs) == list:
            if all(type(item) == str for item in attrs):
                return {key: getattr(self, key)
                        for key in attrs if hasattr(self, key)}
        return self.__dict__
