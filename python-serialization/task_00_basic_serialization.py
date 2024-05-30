#!/usr/bin/python3
"""Module to seralize json and deserialize"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Function to serialize from dictionary

    Args:
        data: python object
        filename: name of file to save
    """
    
    with open(filename, mode='w', encoding="utf") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Function to serialize from dictionary

    Args:
        filename: name of file to save
    Returns:
        returns python object
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        dic = json.load
    return dic
