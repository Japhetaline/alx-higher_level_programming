#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints list of anything, but only prints integers
    Returns the amount of integers printed
    """

    character = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            character += 1
        except (ValueError, TypeError):
            continue

        print()
        return character
