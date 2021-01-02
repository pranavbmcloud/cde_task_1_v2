"""Module tests functionalty in clean.py"""


import unittest


class TestJSONCleaner(unittest.TestCase):
    """Tests functionality of the json cleaner"""
    def setUp(self) -> None:
        with open('./tests/json_testing_sample.json', 'r') as f:
            self.json_raw_data = f.readlines()

        self.cleaned_json_data = [line.replace("'", '"') for line in self.json_raw_data]

    def test_json_clean_double_quotes(self):
        self.assertEqual(JSONCleaner.clean_double_quotes(self.json_raw_data), self.cleaned_json_data)
