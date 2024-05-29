#!/usr/bin/python3
""" serialization and deserialization using XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        function to serialization

        Args:
            dictionary: Dictionary to serialize
            filename: filename to save to
    """

    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
        function to serialization

        Args:
            dictionary: Dictionary to deserialize
            filename: filename to save to
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
