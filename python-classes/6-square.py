#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Represntes square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.postion = position
    """Initialize a new square.

    Args:
    size (int): The size of the new square.
    position (int, int): Position of the square
    """

    @porperty
    def size(self):
        """get/set the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """current position of square"""
        return (self.__position)

    @postion.setter
    def position(self, value):
        if (not isinstance(value, tuple)) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) 
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return are of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square using # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
