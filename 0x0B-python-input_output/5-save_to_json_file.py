#!/usr/bin/python3
"""
@author: Damassoh Japhet
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file using
    a JSON representation
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
