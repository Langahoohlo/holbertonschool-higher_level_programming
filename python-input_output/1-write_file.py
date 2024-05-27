#!/usr/bin/python3
"""Module to write function"""


def write_file(filename="", text=""):
    """Function to overwrite file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
