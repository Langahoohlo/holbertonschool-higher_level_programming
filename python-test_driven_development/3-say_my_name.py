#!/usr/bin/python3
"""
    Function divides all elements of a matrix

    Example:
       first_name = "Langa"
       last_name = "Hoohlo"

       say_my_name(first_name, last_name)

       Langa Hoohlo
"""


def say_my_name(first_name, last_name=""):
    """
        Args:
            first_name: first name
            last_name: second name

        Returns:
            A sentence with the first and last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}" .format(first_name, last_name))
