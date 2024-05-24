#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """
    This class defines a Rectangle with width and height attributes,
    and tracks the number of instances.
    """

    # Public class attributes
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initializes an instance of Rectangle.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        """
        Gets the width of the Rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Sets the width of the Rectangle.

        Args:
            value (int): The width of the rectangle.

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
        """
        Gets the height of the Rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Sets the height of the Rectangle.

        Args:
            value (int): The height of the rectangle.

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
        Returns a string representation of the Rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width
             for _ in range(self.__height)]
        )

    def __repr__(self) -> str:
        """
        Returns a formal string representation of the Rectangle.

        Returns:
            str: The formal string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted and
        decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2) -> 'Rectangle':
        """
        Compares the area of two rectangles and returns the one with the
        larger area. If they have the same area, returns rect_1.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def get_number_of_instances(cls) -> int:
        """
        Returns the current number of Rectangle instances.

        Returns:
            int: The number of Rectangle instances.
        """
        return cls.number_of_instances
