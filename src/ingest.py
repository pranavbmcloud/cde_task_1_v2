"""Module handles ingesting of data from different sources

Data could originate from many sources, exmaples:
File from local file system
File from online url
API response
NoSQL tables

This module shall handle ingesting of the data in raw format into a Python list
"""


def check_file_exists(func):
    def wrap(filename):
        try:
            f = open(filename)
        except FileNotFoundError:
            return None
        else:
            f.close()
            return func(filename)
    return wrap


@check_file_exists
def local_ingest(filepath):
    """Handles ingesting of data from local filesystem

    :parameter
    filepath : str
        filepath of a file on the local filesystem

    :returns
    list
        contents of file, with each line represented as one item in the list
    """
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data
