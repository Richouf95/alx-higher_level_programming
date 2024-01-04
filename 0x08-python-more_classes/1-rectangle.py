#!/usr/bin/python3
"""
    Define class Rectangle
"""


class Rectangle:
    """
        This represente a Rectangle
    """

    def __init__(self, w=0, h=0):
        """
            Initialize a new Rectangle
            Args:
                h (int): Rectangle height
                w (int): Rectangle width
        """
        self.__height = h
        self.__width = w

    def _getWidth(self):
        """
            Width Getter
        """
        return self.__width

    def _setWidth(self, newWidth):
        """
            Width Setter
        """
        if not isinstance(newWidth, int):
            raise TypeError("width must be an integer")
        if newWidth < 0:
            raise ValueError("width must be >= 0")
        self.__width = newWidth

    def _getHeight(self):
        """
            Height Getter
        """
        return self.__height

    def _setHeight(self, newHeight):
        """
            Height Setter
        """
        if not isinstance(newHeight, int):
            raise TypeError("height must be an integer")
        if newHeight < 0:
            raise ValueError("height must be >= 0")
        self.__height = newHeight

    width = property(_getWidth, _setWidth)
    height = property(_getHeight, _setHeight)
