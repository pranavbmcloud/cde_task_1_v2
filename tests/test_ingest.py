"""Module tests functionalty in ingest.py"""


import unittest
from src.ingest import local_ingest


class TestLocalIngest(unittest.TestCase):
    """Tests local ingest functionality"""
    def test_local_ingest_without_filepath_raises_TypeError(self):
        with self.assertRaises(TypeError):
            local_ingest()

    def test_local_ingest_should_return_file_data(self):
        testing_file = "./tests/ingest_testing_sample.txt"
        expected_data = ['this is\n', 'a simple\n', 'text file\n', 'for testing']
        self.assertEqual(local_ingest(testing_file), expected_data)
