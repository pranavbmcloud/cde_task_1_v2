"""Module tests functionalty in process.py"""


import unittest, json
from src.process import json_process, processors, text_process
from src.file_type import get_data_type


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


class TestProcessors(unittest.TestCase):
    """Tests Processors returned based on Data Type"""
    def test_processor_returns_json_processor_for_json(self):
        testing_file = "./tests/json_testing_sample.json"
        file_type = get_data_type(testing_file)
        self.assertEqual(processors[file_type], json_process)

    def test_processor_returns_text_processor_for_text(self):
        testing_file = "./tests/ingest_testing_sample.txt"
        file_type = get_data_type(testing_file)
        self.assertEqual(processors[file_type], text_process)
