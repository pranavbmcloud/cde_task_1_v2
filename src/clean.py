"""Module handles cleaning of raw data Python list created in the ingest.py module

Data might need to be cleaned, exmaples:
Single quotes instead of double quotes in JSON
Response spanning multiple lines instead of a single line in text files


This module shall handle cleaning of the raw data Python list and return a cleaned Python list

Implemented cleaners:
Replace single quotes in json with double quotes
"""


from src.file_type import DataType


class JSONCleaner:
    """Class with all json cleaning methods"""
    @classmethod
    def clean_double_quotes(self, data):
        """Cleans double quotes from raw json data

        the json loads method makes it easy to load json as dict from file
        The json needs to be dict as that enables the next flattening process
        but json.loads() method requires single quotes rather than double quotes
        """
        return [line.replace("'", '"') for line in data]


cleaners = {DataType.JSON: JSONCleaner.clean_double_quotes}
