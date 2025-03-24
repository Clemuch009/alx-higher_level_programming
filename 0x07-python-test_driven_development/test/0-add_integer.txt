#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Returns the sum of two integers.

    Args:
        a (int, float): First number.
        b (int, float, optional): Second number, defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(10)
        108
        >>> add_integer(10.5, 2.7)
        12
        >>> add_integer(-3, 5)
        2
        >>> add_integer("10", 5)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
        >>> add_integer(2, 56)
        58
        >>> add_integer(10, "hello")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

