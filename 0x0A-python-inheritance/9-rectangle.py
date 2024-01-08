#!/usr/bin/python3
"""
    Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class
    """
    def __init__(self, width, height):
        """
            Rectangle initializing
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Rectangle area
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
            Rectangle respresentation
        """
        representation = ""
        representation += "["
        representation += str(self.__class__.__name__)
        representation += "] "
        representation += str(self.__width)
        representation += "/"
        representation += str(self.__height)
        
        return representation
