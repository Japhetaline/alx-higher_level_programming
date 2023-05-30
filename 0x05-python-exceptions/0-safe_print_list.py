#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints list of anything, but only prints integars
    Returns the amount of integars printed
    """

    characters = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            characters = characters + 1
        except Exception:
            continue
        print()
        return characters
