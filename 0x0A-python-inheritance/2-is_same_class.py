#!/usr/bin/pyhton3
"""
Function return True if object is instance otherwise
return false
"""


def is_same_class(obj, a_class):
    """
    Check if two objects are the same class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
