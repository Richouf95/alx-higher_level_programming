#!/usr/bin/python3
"""
    Define class Rectangle
"""


class Rectangle:
    """
        This represente a Rectangle
        Attributes:
            number_of_instances (int): number of instances
            print_symbol (any): symbole use to print a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, w=0, h=0):
        """
            Initialize a new Rectangle
            Args:
                h (int): Rectangle height
                w (int): Rectangle width
        """
        self.__height = h
        self.__width = w
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
            Return the area of the Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            Return the Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
            Print the Rectangle width #
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        representation = ""
        representation += "Rectangle("
        representation += str(self.__width)
        representation += ", "
        representation += str(self.__height)
        representation += ")"
        return representation

    def __del__(self):
        """
            Delete a instance and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    width = property(_getWidth, _setWidth)
    height = property(_getHeight, _setHeight)
