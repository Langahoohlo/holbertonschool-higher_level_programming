#!/usr/bin/python3
"""Defines a class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
