#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
The function returns a list of lists representing the triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        current = []
        for j in range(i + 1):
            if j == 0 or j == i:
                current.append(1)
            else:
                current.append(
                    pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
                )

        pascal_triangle.append(current)

    return pascal_triangle
