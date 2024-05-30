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
    
    try:
        with open(filename, mode='wb') as f:
            pickle.dump(data, f)
    except:
        return None


def load_and_deserialize(filename):
    """
    Function to serialize from dictionary

    Args:
        filename: name of file to save
    Returns:
        returns python object
    """

    try:
        with open(filename, mode="rb") as f:
            return pickle.load(f)
    except:
        return None
