#!/usr/bin/python3

"""
    This is our Square class module
"""


class Square:
    """
        This is our Class Square"
    """
    def __init__(self, s=0, p=(0, 0)):
        """
            Constructor.
            Args:
                s: square size
                position: square position
        """
        self.__size = s
        self.__position = p

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

    def _getPosition(self):
        """
            Getter property for Position attribute
        """
        return self.__position

    def _setPosition(self, newPosition):
        """
            Setter property for Position attribute
        """
        if (not isinstance(newPosition, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(newPosition) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in newPosition):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(x >= 0 for x in newPosition):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = newPosition

    def area(self):
        """
            This function return the current square area
        """
        squareArea = self.size ** 2
        return squareArea

    size = property(_getSize, _setSize)
    position = property(_getPosition, _setPosition)

    def my_print(self):
        """
            Function to print a square
        """
        if self.size == 0:
            return print("")

        for x in range(0, self.position[1]):
            print("")
        for y in range(0, self.size):
            for z in range(0, self.position[0]):
                print(" ", end="")
            for a in range(0, self.size):
                print("#", end="")
            print("")
