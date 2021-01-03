"""Module tests functionality in src/flatten.py"""


import unittest
from src.flatten import flatten_dict, flatteners
from src.file_type import get_data_type


class TestFlatten(unittest.TestCase):
    """Tests the dict flattening functionality"""
    def setUp(self) -> None:
        self.sample_dict = {
            'key1': {
                'nested_key1': 'nested_value1',
                'nested_key2': [
                    'nested_value2', {
                        'deep_nested_key1': 'deep_nested_val1',
                        'deep_nested_key2': 'deep_nested_val2'
                    }
                ]
            },
            'key2': [
                {
                    'nested_key3': 'nested_value4'
                }
            ],
            'key3': 'value1'
        }
        self.flattened_dict = {
            'key1_nested_key1': 'nested_value1',
            'key1_nested_key2_0': 'nested_value2',
            'key1_nested_key2_1_deep_nested_key1': 'deep_nested_val1',
            'key1_nested_key2_1_deep_nested_key2': 'deep_nested_val2',
            'key2_0_nested_key3': 'nested_value4',
            'key3': 'value1'
        }

    def test_flatten(self):
        self.assertEqual(flatten_dict(self.sample_dict), self.flattened_dict)


class TestFlatteners(unittest.TestCase):
    """Tests flatenner returned based on Data Type"""
    def test_flattener_returns_dict_flattener_for_json(self):
        testing_file = "./tests/json_testing_sample.json"
        file_type = get_data_type(testing_file)
        self.assertEqual(flatteners[file_type], flatten_dict)
