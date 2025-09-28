#!/usr/bin/python3
"""
multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix
    
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]

    >>> matrix_mul(([1, 2], [3, 4]), [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    TypeError:  m_a must be a list
    
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], (3, 4)])
    Traceback (most recent call last):
        ...
    TypeError:  m_b must be a list of lists

    >>> matrix_mul([], [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    ValueError: m_a can't be empty

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 'h']])
    Traceback (most recent call last):
        ...
    TypeError:  m_b should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4, 6]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_a must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]], [1, 2])
    Traceback (most recent call last):
        ...
    ValueError: m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list ")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if any(not isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == m_a[0] for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == m_b[0] for row in m_b):
        raise: TypeError("each row of m_b must be of the same size")

    clmns = 0
    rows = len(m_b[0])

    for row in m_b:
        row += 1
    if rows != clmns:
        raise ValueError("m_a and m_b can't be multiplied")

