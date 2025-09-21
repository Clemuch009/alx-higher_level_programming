#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            end_char = " " if i < len(row) - 1 else ""
            print("{}".format(row[i]), end=end_char)
        print()  # new line after each row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)

