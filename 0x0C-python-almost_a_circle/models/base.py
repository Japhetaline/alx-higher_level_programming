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
