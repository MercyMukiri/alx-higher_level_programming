#!/usr/bin/python3
"""
2-matrix_divided module

This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ This function divides the integer/float numbers of a matrix
    Args: matrix: list of a lists of integers/floats
          div: number (integer or float) which divides the matrix
    Returns: A new matrix with the result of the division
    Raises: TypeError: If the elements of the matrix aren't lists
                       If the elements of the matrix aren't integers/floats
                       If each row of the matrix is not of the same size
                       If div is not an integer/float number
            ZeroDivisionError: If div is zero
    """

    new_list = []
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(message)

    for row in matrix:
        size = []
        if(len(matrix[0]) != len(row)):
            raise TypeError("Each row of the matrix must have the same size")
        for column in range(len(row)):
            if type(row[column]) not in [int, float]:
                raise TypeError(message)

            size.append(round(((row[column]) / div), 2))

        new_list.append(size)

    return new_list
