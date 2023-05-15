#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers to STDOUT"""
    for queue in matrix:
        queue_len = len(queue)
        for k in range(queue_len):
            if k != queue_len - 1:
                print("{:d}".format(queue[k]), end=' ')
            else:
                print("{:d}".format(queue[k]), end='')
                print()
