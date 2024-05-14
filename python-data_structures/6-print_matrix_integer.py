#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    length, i, = len(matrix), 0

    if len(matrix) == 0:
        print("\n")

    while i < length:
        row, j = matrix[i], 0
        l = len(row)

        while j < l:
            if j == l - 1:
                print("{:d}" .format(row[j]))

            else:
                print("{:d}" .format(row[j]), end=" ")

            j += 1

        i += 1
