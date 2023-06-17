#!/usr/bin/python3
"""
@author: Damassoh Japhet
"""

import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function to manage id attribute in all
        fucture classes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation

        Args:
        list_dictionaries (list): A list of dictionaries.

        Returns:
        str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list instances
        to a file.

        Args:
        list_objs (list): List of instances.

        Returns:
        None
        """
        filename = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for k in list_objs:
                string.append(cls.to_dictionary(k))
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(cls.to_json_string(string))
