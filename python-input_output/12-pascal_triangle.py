#!/usr/bin/python3
"""triangulo pascal"""


def pascal_triangle(n):
    """genera untriangulo pascal con n final"""
    if n <= 0:
        return []

    triangulo = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangulo[i-1][j-1] + triangulo[i-1][j])
        triangulo.append(row)
    return triangulo
