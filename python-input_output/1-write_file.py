#!/usr/bin/python3
"""Module to write function"""


def write_file(filename="", text=""):
    """Function to iverwrite file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
