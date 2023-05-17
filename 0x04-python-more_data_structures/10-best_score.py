#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest valaue
    """
    max_use = 0
    champ = None
    if type(a_dictionary) is dict:
        for pointer, use in a_dictionary.items():
            if use >= max_use:
                max_use = use
                champ = pointer
                return champ
