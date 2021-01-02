"""This module tests functionality in the source_type.py module"""


import unittest
from src.source_type import get_source_type, DataSource


class TestSourceType(unittest.TestCase):
    """Tests Source Type related functionality in the main.py module"""
    def setUp(self) -> None:
        self.input_url = "http://www.somedomain.com/path/input_file.json"
        self.local_file = "file 01.json"

    def test_url_input_should_return_url_datasource(self):
        source_type = get_source_type(self.input_url)
        self.assertEqual(source_type, DataSource.URL)

    def test_local_input_should_return_local_datasource(self):
        source_type = get_source_type(self.local_file)
        self.assertEqual(source_type, DataSource.LOCAL)
