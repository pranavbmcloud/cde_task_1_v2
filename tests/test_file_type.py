"""This module tests functionality in the file_type.py module"""


import unittest


class TestMainSourceType(unittest.TestCase):
    """Tests Source Type related functionality in the main.py module"""
    def setUp(self) -> None:
        self.json_input_url = "http://www.somedomain.com/path/input_file.json"
        self.json_local_file = "file 01.json"
        self.xml_input_url = "http://www.somedomain.com/path/input_file.xml"
        self.xml_local_file = "file 01.xml"
        self.text_input_url = "http://www.somedomain.com/path/input_file.txt"
        self.text_local_file = "file 01.txt"

    def test_json_input_file_should_return_json_datatype(self):
        file_type = get_data_type(self.json_local_file)
        self.assertEqual(file_type, DataType.JSON)
