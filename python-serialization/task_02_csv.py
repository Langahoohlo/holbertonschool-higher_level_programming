#!/usr/bin/python3
"""read csv and convert to json"""
import csv
import json


def convert_csv_to_json(csvdata):
    """function to convert csv to json

    Args:
        data: csv file to converted to json

    """

    data = {}
    try:
        with open(csvdata, 'r', encoding='utf-8') as cs_v:
            csvReader = csv.DictReader(cs_v)
            for row in csvReader:
                data.append(row)

    except FileNotFoundError:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as jsondata:
            json.dump(data, jsonfile, indent=4)
    except:
        return False
    return True
