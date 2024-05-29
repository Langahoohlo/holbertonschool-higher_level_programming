#!/usr/bin/python3
"""module to have a custom objectclass"""
import pickle


class CustomObject:
    """ customObject class
    Args:
        name: string
        age: integer
        is_student: boolen
    """

    def __init__(self, name, age, is_student):
        """function initializes object"""
        self.name = name
        self.age = age
        self.is_student = student

    def display(self):
        """functin to print"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.age} ")

    def serialize(self, filename):
        """function to serialize instance of object"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """function to return inctance of customObject"""
        with open(filename, "rb") as f:
            r = pickle.load(f)
        return f
