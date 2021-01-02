"""Module tests functionalty in process.py"""


import unittest, json
from src.process import json_process


class TestJSONProcess(unittest.TestCase):
    """Tests JSON processing functionality"""
    def setUp(self) -> None:
        self.expected_data = [{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
                                        {'firstName': 'Anna', 'lastName': 'Smith'},
                                        {'firstName': 'Peter', 'lastName': 'Jones'}]}]

    def test_json_process_cleaned_file(self):
        self.assertEqual(json_process('./tests/json_process_testing.json'), self.expected_data)

    def test_json_process_malformed_file(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            json_process('./tests/json_testing_sample.json')
