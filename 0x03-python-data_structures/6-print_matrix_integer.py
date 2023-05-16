#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """
    prints a matrix of integers to STDOUT
    """
    for queue in matrix:
        for vertical in queue:
            print("{:d}".format(vertical),end="" if vertical !=queue[-1]else "")
            print()
