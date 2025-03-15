#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    
    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.
    
    Returns:
        list of lists: The product of m_a and m_b.
    
    Raises:
        TypeError: If inputs are not lists of lists of integers or floats.
        ValueError: If matrices are empty or cannot be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])
    
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = [[sum(m_a[i][k] * m_b[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(rows_a)]
    
    return result
