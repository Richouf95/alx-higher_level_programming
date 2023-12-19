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
        self.__size = s

    def _getSize(self):
        """
            Getter property for size attribute
        """
        return self.__size

    def _setSize(self, newSize):
        """
            Setter property for size attribute
        """
        if not isinstance(newSize, int):
            raise TypeError("size must be an integer")
        elif newSize < 0:
            raise TypeError("size must be >= 0")
        self.__size = newSize

    def area(self):
        """
            This function return the current square area
        """
        squareArea = self.size ** 2
        return squareArea

    size = property(_getSize, _setSize)
