#!/usr/bin/python3
"""
@author: Damassoh Japhet
"""

import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Writing object to a text file using JSON representation
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Creating an object from a JSON representation
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj

    filename = "add_item.json"

    manage_list.append(sys.argv[1:])
    save_to_json_file(manage_list, filename)
