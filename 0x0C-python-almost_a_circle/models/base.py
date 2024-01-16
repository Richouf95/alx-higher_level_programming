#!/usr/bin/python3
"""
    This is the Base Class
"""


import json
import csv
import turtle


class Base:
    """
        Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize an instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def from_json_string(json_string):
        """
            Json serialization
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    def to_json_string(list_dictionaries):
        """
            JSON serialization of a list of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
            Write the JSON serialization file
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as fic:
            if list_objs is None:
                fic.write("[]")
            else:
                data = [o.to_dictionary() for o in list_objs]
                fic.write(Base.to_json_string(data))

    def create(cls, **dictionary):
        """
            create a class instance
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instanceData = cls(1, 1)
            else:
                instanceData = cls(1)
            instanceData.update(**dictionary)
            return instanceData

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def save_to_file_csv(cls, list_objs):
        """
            Save file csv
        """
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "a") as fic:
            if list_objs is None or list_objs == []:
                fic.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                writer = csv.DictWriter(fic, fieldnames=keys)
                for data in list_objs:
                    writer.writerow(data.to_dictionary())

    def load_from_file_csv(cls):
        """
            Load file csv
        """
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, "r", newline="") as fic:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                data = csv.DictReader(fic, fieldnames=keys)
                data = [dict([key, int(value)] for key, value in item.items())
                        for item in data]
                return [cls.create(**obj) for obj in data]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        tu = turtle.Turtle()
        tu.screen.bgcolor("#C75FAF")
        tu.pensize(3)
        tu.shape("turtle")

        tu.color("#ffffff")
        for rectangle in list_rectangles:
            tu.showturtle()
            tu.up()
            tu.goto(rectangle.x, rectangle.y)
            tu.down()
            for j in range(2):
                tu.forward(rectangle.width)
                tu.left(90)
                tu.forward(rectangle.height)
                tu.left(90)
            tu.hideturtle()

        tu.color("#FF7F7F")
        for square in list_squares:
            tu.showturtle()
            tu.up()
            tu.goto(square.x, square.y)
            tu.down()
            for j in range(2):
                tu.forward(square.width)
                tu.left(90)
                tu.forward(square.height)
                tu.left(90)
            tu.hideturtle()

        turtle.exitonclick()

    from_json_string = staticmethod(from_json_string)
    to_json_string = staticmethod(to_json_string)
    save_to_file = classmethod(save_to_file)
    create = classmethod(create)
    save_to_file_csv = classmethod(save_to_file_csv)
    load_from_file_csv = classmethod(load_from_file_csv)
    draw = staticmethod(draw)
