#!/usr/bin/python3
"""
    Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        Square class
    """
    def __init__(self, size):
        """
            Initializing
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
            Squarre area
        """
        area = self.__size ** 2
        return area
