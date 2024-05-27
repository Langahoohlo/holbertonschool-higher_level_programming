#!/usr/bin/python3
"""Module to write function"""


def write_file(filename="", text=""):
    """Function to overwrite file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
