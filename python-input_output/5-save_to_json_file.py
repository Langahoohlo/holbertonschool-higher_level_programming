#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write an object to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
