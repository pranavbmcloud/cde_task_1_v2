"""Module tests functionalty in write.py"""


import unittest
from src.write import simple_writer


class TestWriteSimple(unittest.TestCase):
    """Tests functionality in the write.py module"""
    def setUp(self) -> None:
        self.sample_data = ["line 1\n", "line 2\n", "line 3\n"]
        self.expected_data = ["line 1\n", "line 2\n", "line 3\n"]
        self.output_file_name = "./tests/output_sample_file.txt"
        simple_writer(self.sample_data, self.output_file_name)

    def test_simple_write(self):
        with open(self.output_file_name, 'r') as f:
            data = f.readlines()
        self.assertEqual(data, self.expected_data)
