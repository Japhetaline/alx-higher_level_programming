#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates or add key/value into a dictionary
    then returns a new copy
    """
    a_dictionary.update({key: value})
    return (a_dictionary.copy())
