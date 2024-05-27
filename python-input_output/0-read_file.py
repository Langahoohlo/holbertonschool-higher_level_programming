#!/usr/bin/python3
"""Module to read a file from argument"""


def read_file(filename=""):
    """Function to read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read, end="")
