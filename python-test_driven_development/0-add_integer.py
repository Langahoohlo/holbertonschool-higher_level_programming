#!/usr/bin/python3

"""
    Function divides all elements of a matrix

    Example:
       a = 7
       b = 20

       add_integer(a, b)

       27
"""


def add_integer(a, b=98):
    """
        Args:
            a: first integer
            b: second integer

        Returns:
            Sum of the two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if a is type(float):
        int(a)
    if b is type(float):
        int(b)
    return int(a + b)
