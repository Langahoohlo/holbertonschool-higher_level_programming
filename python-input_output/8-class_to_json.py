#!/usr/bin/python3
"""Object class to JSON"""
import json


def class_to_json(obj):
    """Return a data structure"""
    return obj.__dict__
