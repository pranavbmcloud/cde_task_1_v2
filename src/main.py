"""Main module that directs the workflow"""


import re
from enum import Enum


DataSource = Enum('DataSource', 'URL LOCAL')


def is_url(filepath):
    url_regex = re.compile('http*')
    if url_regex.match(filepath):
        return True
    else:
        return False

def get_source_type(file_source):
    if is_url(file_source):
        data_source = DataSource.URL
    else:
        data_source = DataSource.LOCAL
    return data_source