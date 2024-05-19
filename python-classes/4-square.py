#!/usr/bin/python3

"""Define class square"""


class Square:
    """Represents square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
        size (int): The size of square
        """
        self.size = size

    @property
    def size(self):
        """get/set current of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """return the area of square"""
        return (self.__size__ * self.__size)
