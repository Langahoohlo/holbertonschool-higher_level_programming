#!/usr/bin/python3
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, mode='wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, mode="rb") as f:
        return pickle.load(f)
