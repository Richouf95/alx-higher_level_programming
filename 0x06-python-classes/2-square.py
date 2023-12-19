#!/usr/bin/python3

"""
    This is our Square class module
"""


class Square:
    """
        This is our Class Square"
    """
    def __init__(self, s=0):
        """
            Constructor.
            Args:
                s: square size
        """
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        elif s < 0:
            raise TypeError("size must be >= 0")
        self.__size = s
