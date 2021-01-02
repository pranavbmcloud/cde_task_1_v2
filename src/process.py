"""Module handles processing of data

Some data formats provide easy to process methods to read data, example:
json.loads()
xml.etree.ElementTree.parse()

This module shall handle processing of the data
"""


import json
from src.file_type import DataType


def json_process(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return [json.loads(line) for line in data]


processors = {DataType.JSON: json_process}
