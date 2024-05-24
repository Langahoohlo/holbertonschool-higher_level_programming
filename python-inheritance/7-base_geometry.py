#!/usr/bin/python3
"""
Module consists of a class name 'BaseGeometry'
"""


class BaseGeometry:
    """Class of BaseGeometry"""
    def area(self):
        """Method that raises Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
