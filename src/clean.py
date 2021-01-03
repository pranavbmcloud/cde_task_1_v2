"""Module handles cleaning of raw data Python list created in the ingest.py module

Data might need to be cleaned, exmaples:
Single quotes instead of double quotes in JSON
Response spanning multiple lines instead of a single line in text files


This module shall handle cleaning of the raw data Python list and return a cleaned Python list

Implemented cleaners:
Replace single quotes in json with double quotes
"""


import re
from src.file_type import DataType


class JSONCleaner:
    """Class with all json cleaning methods"""
    @staticmethod
    def clean_single_quotes(data):
        """Cleans double quotes from raw json data

        the json loads method makes it easy to load json as dict from file
        The json needs to be dict as that enables the next flattening process
        but json.loads() method requires double quotes rather than single quotes
        """
        return [line.replace("'", '"') for line in data]


class TextCleaner:
    """Handles all text cleaning activities"""
    @staticmethod
    def get_header(data_row):
        """Used by the text_clean method to get header"""
        header = [item.replace('"', "") for item in data_row.split(sep=",")]
        new_header = ",".join(item for item in header)
        formatted_header = new_header.rstrip()
        return formatted_header

    @staticmethod
    def consolidate_product_data_to_one_line(data):
        """used by text_clean method to consolidate product data"""
        order_id = re.compile(r'\d\d\d\d\d\d\d')
        my_list = []
        for i, item in enumerate(data):
            if order_id.match(item):
                my_list.append(item)
            else:
                my_list[-1] += item
        return my_list

    @staticmethod
    def text_clean(data):
        """Cleans text files for further processing

        Related product data could span multiple lines, this method puts each product data on single lines
        Cleans un-necessary double quotes
        Cleans additional new lines or spaces at the end of line

        :parameter
        data : list
            raw list with each item consisting of one line of input file

        :returns
        cleaned_data : list
            list with header as first item, 1 line per product data
        """
        first_line = 0
        second_line = 1

        formatted_header = TextCleaner.get_header(data[first_line])

        product_data_double_quotes_cleaned = [item.replace('"', "") for item in data[second_line:]]
        product_data = [item.rstrip() for item in product_data_double_quotes_cleaned]
        consolidated_product_data = TextCleaner.consolidate_product_data_to_one_line(product_data)

        consolidated_product_data.insert(0, formatted_header)
        cleaned_data = [item + "\n" for item in consolidated_product_data]
        return cleaned_data


cleaners = {DataType.JSON: JSONCleaner.clean_single_quotes, DataType.TEXT: TextCleaner.text_clean}
