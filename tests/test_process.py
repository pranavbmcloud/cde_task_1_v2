"""Module tests functionalty in process.py"""


import unittest
import json
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


class TestTextProcess(unittest.TestCase):
    """Tests Text processing functionality"""
    def test_text_process_should_return_file_data(self):
        testing_file = "./tests/ingest_testing_sample.txt"
        expected_data = ['this is\n', 'a simple\n', 'text file\n', 'for testing']
        self.assertEqual(text_process(testing_file), expected_data)
