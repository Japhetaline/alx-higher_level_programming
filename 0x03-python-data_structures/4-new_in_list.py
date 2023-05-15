#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    """
    Replace an element in a list at a specific position
    without modifying the original list
    """

    if idx >= len(my_list) or idx < 0:
        return (my_list)
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
