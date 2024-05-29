#!/usr/bin/python3
"""Module to seralize json and deserialize"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Function to serialize from dictionary

    Args:
        data: python object
        filename: name of file to save
    """

    with open(filename, mode='w') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """
    Function to serialize from dictionary

    Args:
        filename: name of file to save
    Returns:
        returns python object
    """

    with open(filename, mode="r") as f:
        return pickle.load(f)
