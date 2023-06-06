#!/usr/bin/python3
"""
writing a class with no class or object
attribute
"""


class LockedClass:
    """
    A locked class that only lets the user dynamically create the
    instance attribute 'first_name'
    """
    __slots__ = ['first_name']
