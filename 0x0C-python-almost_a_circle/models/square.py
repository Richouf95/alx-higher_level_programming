#!/usr/bin/python3
"""
    Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initializing a square
        """
        super().__init__(size, size, x, y, id)

    def getSize(self):
        """
            Size Getter
        """
        return self.width

    def setSize(self, newSize):
        """
            Size Setter
        """
        setattr(self, "width", newSize)
        setattr(self, "height", newSize)

    def update(self, *args, **kwargs):
        """
            Update the instance
        """
        if args and len(args) != 0:
            i = 0
            while i < len(args):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        setattr(self, 'id', args[i])
                elif i == 1:
                    setattr(self, 'size', args[i])
                elif i == 2:
                    setattr(self, 'x', args[i])
                elif i == 3:
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
                        setattr(self, 'id', value)
                elif key == "size":
                    setattr(self, 'size', value)
                elif key == "x":
                    setattr(self, 'x', value)
                elif key == "y":
                    setattr(self, 'y', value)
                else:
                    pass

    def to_dictionary(self):
        """
            The dict representation
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def to_dictionary(self):
        """
            Dictionary representation of the Square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
            String representation of a Square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x, self.y,
                self.width)

    size = property(getSize, setSize)
