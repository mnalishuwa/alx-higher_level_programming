#!/usr/bin/python3

"""
Matrix division function
"""


def matrix_divided(matrix, div):
    """
    Matrix division function:

    Arguments:
        matrix - list of lists of equal length
        div - int or float, != 0

    Raises:
        TypeError
        ZeroDivisionError

    Return:
        Matrix
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_msg)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_msg)
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for number in row:
            if type(number) not in (int, float):
                raise TypeError(err_msg)
            new_row.append(round(number / div, 2))
        new_matrix.append(new_row)

    return new_matrix
