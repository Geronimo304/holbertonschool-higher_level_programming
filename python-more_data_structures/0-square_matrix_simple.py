#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_nueva = []
    for i in matrix:
        nueva = []
        for j in i:
            nueva.append(j ** 2)
        matrix_nueva.append(nueva)
    return matrix_nueva