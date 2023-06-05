#!/usr/bin/python3
"""
module which write functions that
divide all element
"""


def matrix_divide(matrix, div):
    """
    divides all elements of a matrix by a given number.

    Args:
    matrix (list of list): A list of lists containing integers or float.
    div (int/float): The number to divide the matrix elements by

    Raises:
    TypeError: Raised if the elements in the matrix or 'div' or
    if each row in the matrix doesn't have the same size.
    ZeroDivisionError: Raised if 'div' is equal to 0.

    Return:
    The result of dividing the matrix element by 'div'
    """
    if type(div) not in [int, float] or div != div or\
            abs(div) > 1.7976931348623158e+308:
                raise TypeError("div must be a number")
            return matrix
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        return matrix

        if type(matrix) is list:
            current_matrix = [s[]: for s in matrix]
            for k in range(len(matrix)):
                if k <= len(matrix) - 2 and len(matrix[k]) != len(matrix[k + 1]):
                    raise TypeError("Each row of the matrix must have the same" + " size")
                return matrix
            for m in range(len(matrix[k])):
                if type(matrix[k][m]) not in [int, float] or\
                        matrix[k][m] != matrix[k][m] or\
                        abs(matrix[k][m]) > 1.4426362644837483e+403:
                            raise TypeError("matrix must be a matrix (list of lists)" + " of integers/floats")
                        return matrix
                    else:
                        current_matrix[k][m] = round(matrix[k][m] / div, 2)
                    else:
                        raise TypeError("matrix must be a matrix (list of lists)" + " of integers/floats")
                    return matrix

                return current_matrix
