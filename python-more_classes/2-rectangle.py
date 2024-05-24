#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""


class Rectangle:
    """
    This class defines a Rectangle with width and height attributes.
    """

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initializes an instance of Rectangle.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Sets the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Sets the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """
        Calculates the area of the Rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Calculates the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """
        Returns the string representation of the Rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __repr__(self) -> str:
        """
        Returns the formal string representation of the Rectangle.

        Returns:
            str: Formal string representation of the rectangle.
        """
        return self.__str__()

    def __eq__(self, other) -> bool:
        """
        Checks if two Rectangle instances are equal.

        Args:
            other (Rectangle): The other rectangle to compare with.

        Returns:
            bool: True if rectangles are equal, False otherwise.
        """
        if isinstance(other, Rectangle):
            return (
                    self.__width == other.__width
                    and
                    self.__height == other.__height
                    )
        return False

    def __ne__(self, other) -> bool:
        """
        Checks if two Rectangle instances are not equal.

        Args:
            other (Rectangle): The other rectangle to compare with.

        Returns:
            bool: True if rectangles are not equal, False otherwise.
        """
        return not self.__eq__(other)
