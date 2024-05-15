#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    my_matrix = []
    for row in matrix:
        my_row = [x ** 2 for x in row]
        my_matrix.append(my_row)

    return my_matrix
