#!/usr/bin/python3
"""
    This is the Base Class
"""


import json


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

    from_json_string = staticmethod(from_json_string)
    to_json_string = staticmethod(to_json_string)
    save_to_file = classmethod(save_to_file)
    create = classmethod(create)
