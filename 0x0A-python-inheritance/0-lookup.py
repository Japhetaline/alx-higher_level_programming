#!/bin/python3
"""
This function returns lists of attribute and
method of an object
"""

def lookup(obj):
    """
    Returns all objects in an objects dictionary
    as a LIST
    """
    return dir(obj)
