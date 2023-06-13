#!/usr/bin/python3
"""
@author:Damassoh Japhet
"""

import json


def load_from_json_file(filename):
    """
    Function that create that object from a
    JSON file
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
