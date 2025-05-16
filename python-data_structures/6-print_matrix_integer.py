#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for i in range(len(fila)):
            if i != len(fila) - 1:
                print("{:d}".format(fila[i]), end=" ")
            else:
                print("{:d}".format(fila[i]), end="")
        print()