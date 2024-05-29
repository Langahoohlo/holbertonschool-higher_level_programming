#!/usr/bin/python3
"""read csv and convert to json"""
import csv
import json


def convert_csv_to_json(data):
    """function to convert csv to json
    Args:
        data: csv file to converted to json
    """
    with open(data, 'r', newline='') as cs_v:
        csvReader = csv.DictReader(cs_v)
        info = list(csvReader)

    json_data = json.dumps(info, indent=4)

    with open('info.json', 'w') as jsonfile:
        jsonfile.write(json_data, indent)
