#!/usr/bin/python3
"""Module to JSONIFY an object"""
import json


def to_json_string(my_obj):
    """Module to jsonify argument my_obj"""
    return json.dumps(my_obj)
