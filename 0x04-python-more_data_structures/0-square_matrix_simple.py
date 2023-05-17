#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integars of a matrix
    """
    return ([[(x**2) for x in queue] for queue in matrix])
