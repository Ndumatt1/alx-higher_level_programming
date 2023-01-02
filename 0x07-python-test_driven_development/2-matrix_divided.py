#!/usr/bin/python3
""" This module divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_length = [len(row) for row in matrix]
    if not all(length == row_length[0] for length in row_length):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[0 for row in range(len(matrix[0]))]
                  for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return (new_matrix)
