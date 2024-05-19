#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
2-square.py: a class square
"""


class Square:
    """class square that defines a square
    Attributes:
        attr1 (_Square_Size): Private instance attribute
    """

    def __init__(self, size=0):
        """Initializer with size = 0"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
