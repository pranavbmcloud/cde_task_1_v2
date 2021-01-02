"""Module tests functionalty in clean.py"""


import unittest
from src.clean import JSONCleaner, cleaners
from src.file_type import get_data_type


class TestJSONCleaner(unittest.TestCase):
    """Tests functionality of the json cleaner"""
    def setUp(self) -> None:
        with open('./tests/json_testing_sample.json', 'r') as f:
            self.json_raw_data = f.readlines()

        self.cleaned_json_data = [line.replace("'", '"') for line in self.json_raw_data]

    def test_json_clean_double_quotes(self):
        self.assertEqual(JSONCleaner.clean_double_quotes(self.json_raw_data), self.cleaned_json_data)


class TestCleaners(unittest.TestCase):
    """Tests Cleaners returned based on Data Type"""
    def test_cleaner_returns_json_cleaner_for_json_file(self):
        testing_file = "./tests/json_testing_sample.json"
        file_type = get_data_type(testing_file)
        self.assertEqual(cleaners[file_type], JSONCleaner.clean_double_quotes)
