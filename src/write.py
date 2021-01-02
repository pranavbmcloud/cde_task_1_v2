"""Module handles writing of data

Data might have multiple destinations, example:
Local file system
Web endpoints
Exposed as a REST API

This module shall handle writing of the data based on the output format

Implemented writers:
Local file system
"""


def simple_writer(data, output_file):
    with open(output_file, 'w') as f:
        for line in data:
            f.writelines(line)
