#!/usr/bin/python3
"""
Module: matrix_divided

This module provides a single function, `matrix_divided`, which divides
all elements of a matrix by a given divisor. It validates that the matrix
is a non-empty list of lists containing only integers or floats,
with all rows having the same size.
The division result is rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix
    with results rounded to 2 decimal places.
    """
    if not (
        isinstance(matrix, list)
        and all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    elements_check = all(
        isinstance(num, (int, float)) for row in matrix for num in row
    )
    if not elements_check:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_check = all(len(row) == len(matrix[0]) for row in matrix)
    if not row_check:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
