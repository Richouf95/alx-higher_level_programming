#!/usr/bin/python3
"""
    This is the Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
        This is the Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initilizing an instance
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self._width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self._height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self._x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self._y = y
        super().__init__(id)

    def getWidth(self):
        """
            Width Getter
        """
        return self._width

    def setWidth(self, newWidth):
        """
            Widgth Setter
        """
        if type(newWidth) != int:
            raise TypeError("width must be an integer")
        if newWidth <= 0:
            raise ValueError("width must be > 0")
        self._width = newWidth

    def getHeight(self):
        """
            Height Getter
        """
        return self._height

    def setHeight(self, newHeight):
        """
            Height Setter
        """
        if type(newHeight) != int:
            raise TypeError("height must be an integer")
        if newHeight <= 0:
            raise ValueError("height must be > 0")
        self._height = newHeight

    def getX(self):
        """
            X Getter
        """
        return self._x

    def setX(self, newX):
        """
            X Setter
        """
        if type(newX) != int:
            raise TypeError("x must be an integer")
        if newX < 0:
            raise ValueError("x must be >= 0")
        self._x = newX

    def getY(self):
        """
            Y Getter
        """
        return self._y

    def setY(self, newY):
        """
            Y Setter
        """
        if type(newY) != int:
            raise TypeError("y must be an integer")
        if newY < 0:
            raise ValueError("y must be >= 0")
        self._y = newY

    def area(self):
        """
            Return the area of the Rectangle
        """
        return (self._width * self._height)

    def display(self):
        """
            print the rectangle
        """
        if self._width == 0 or self.height == 0:
            print("")
            return

        [print("") for a in range(self._y)]
        for b in range(self._height):
            [print(" ", end="") for c in range(self._x)]
            [print("#", end="") for d in range(self._width)]
            print("")

    def __str__(self):
        """
            object instance representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self._x, self._y,
                self._width, self._height)

    def update(self, *args, **kwargs):
        """
            Update an instance
        """
        if args and len(args) != 0:
            i = 0
            while i < len(args):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        """self.id = args[i]"""
                        setattr(self, 'id', args[i])
                elif i == 1:
                    """self.width = args[i]"""
                    setattr(self, 'width', args[i])
                elif i == 2:
                    """self.height = args[2]"""
                    setattr(self, 'height', args[i])
                elif i == 3:
                    """self.x = args[3]"""
                    setattr(self, 'x', args[i])
                elif i == 4:
                    """self.y = args[4]"""
                    setattr(self, 'y', args[i])
                else:
                    pass
                i += 1

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        """self.id = value"""
                        setattr(self, 'id', value)
                elif key == "width":
                    """self.width = value"""
                    setattr(self, 'width', value)
                elif key == "height":
                    """self.height = value"""
                    setattr(self, 'height', value)
                elif key == "x":
                    """self.x = value"""
                    setattr(self, 'x', value)
                elif key == "y":
                    """self.y = value"""
                    setattr(self, 'y', value)
                else:
                    pass

    def to_dictionary(self):
        """
            Dictionary representation of instance
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    width = property(getWidth, setWidth)
    height = property(getHeight, setHeight)
    x = property(getX, setX)
    y = property(getY, setY)
