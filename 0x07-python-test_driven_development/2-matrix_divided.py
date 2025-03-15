#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
      
    if not all(isinstance (element, (float,int))for row in matrix for element in row ) :
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == matrix[0] for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance (div , (float, int)):
               raise TypeError("div must be a number")

    if div == 0:
               raise ZeroDivisionError("division by zero")

    new_matrix = [ [round (element/div , 2) for element in row] for row in matrix]


    for row in new_matrix:
               print (row)

    return new_matrix
