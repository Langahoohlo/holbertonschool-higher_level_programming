#!/usr/bin/python3

"""Define class square"""


class Square:
    """Represents square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
        size (int): Size of new square
        """

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the are of the square"""
        return (self.__size * self.__size)
