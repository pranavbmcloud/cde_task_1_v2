"""Module handles writing of data

Data might have multiple destinations, example:
Local file system
Web endpoints
Exposed as a REST API

This module shall handle writing of the data based on the output format

Implemented writers:
Local file system
"""


import csv
from src.file_type import DataType


def simple_writer(data, output_file):
    with open(output_file, 'w') as f:
        for line in data:
            f.writelines(line)


def dict_writer(data, output_file):
    with open(output_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t')
        keys = []
        values = []
        for item in data.keys():
            keys.append(item)
        csvwriter.writerow(keys)
        for item in data.values():
            values.append(item)
        csvwriter.writerow(values)


def list_writer(data, output_file):
    for item in data:
        dict_writer(item, output_file)


writers = {DataType.JSON: list_writer}
