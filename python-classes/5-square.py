#!/usr/bin/python3

"""Define class square"""


class Square:
    """Represents square

    Args:
    size (int): The size of square
    """
    self.size = size

    @property
    def size(self):
        """get/set the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square using # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
