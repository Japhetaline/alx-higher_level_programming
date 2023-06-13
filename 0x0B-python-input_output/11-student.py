#!/usr/bin/python3
"""
@athor: Damassoh Japhet
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        init method for Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        represent of students in json format
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        represent students in json format
        """
        for key, value in json.items():
            setattr(self, key, value)
