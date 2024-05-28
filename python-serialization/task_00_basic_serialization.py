#!/usr/bin/python3
"""Module to seralize json and deserialize"""
import pickle


def serialize_and_save_to_file(data, filename):
    """Function to serialize from deictionary"""
    with open(filename, mode='wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """Function to deciaralize json to dixtionary"""
    with open(filename, mode="rb") as f:
        return pickle.load(f)
