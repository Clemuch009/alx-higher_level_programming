#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides the elements of a matrix by div.
    
    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The number to divide each element by.
    
    Returns:
        list of lists: A new matrix with each element divided by div, rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If all rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Examples:
        >>> matrix_divided([[2, 4, 6], [8, 10, 12], [16, 18, 20]], 2)
        [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [8.0, 9.0, 10.0]]

        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

        >>> matrix_divided("hello", 2)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([[1, 2, 3], [4, 5]], 3)
        Traceback (most recent call last):
        ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], "hello")
        Traceback (most recent call last):
        ...
        TypeError: div must be a number

        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]

