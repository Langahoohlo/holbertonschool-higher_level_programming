#!/usr/bin/python3
"""A module to define the class student"""


class Student:
    """Class for student"""

    def __init__(self, first_name, last_name, age):
        """class to define first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        
    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
