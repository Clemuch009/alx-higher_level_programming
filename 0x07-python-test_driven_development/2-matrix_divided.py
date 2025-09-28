#!/usr/bin/python3
""" function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by div

    >>> matrix = [[1, 2, 3],[4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_1 =  [(1, 2, 3),[4, 5, 6]]

    >>> matrix_divided(matrix_1, 3)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists)

    >>> matrix_2 = [[1, 'b', 3],[4, 5, 6]]

    >>> matrix_divided(matrix_2, 3)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    >>> matrix_divided(matrix, "b")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix_4 = [[1, 2, 4, 3],[4, 5, 6]]

    >>> matrix_divided(matrix_4, 3)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size

    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in row]  for row in matrix]
    return new_matrix
