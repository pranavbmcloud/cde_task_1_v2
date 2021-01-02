"""Module tests functionalty in ingest.py"""


import unittest
from src.ingest import local_ingest, ingesters
from src.source_type import get_source_type, DataSource


class TestLocalIngest(unittest.TestCase):
    """Tests local ingest functionality"""
    def test_local_ingest_without_filepath_raises_TypeError(self):
        with self.assertRaises(TypeError):
            local_ingest()

    def test_local_ingest_should_return_file_data(self):
        testing_file = "./tests/ingest_testing_sample.txt"
        expected_data = ['this is\n', 'a simple\n', 'text file\n', 'for testing']
        self.assertEqual(local_ingest(testing_file), expected_data)

    def test_local_ingest_of_non_existant_file_returns_None(self):
        testing_file = "./tests/ingest_testing_sample.tx"
        self.assertEqual(local_ingest(testing_file), None)


class TestIngesters(unittest.TestCase):
    """Tests ingesters returned based on Data Source Type"""
    def test_ingester_returns_local_ingester_for_local_file(self):
        testing_file = "./tests/ingest_testing_sample.txt"
        source_type = get_source_type(testing_file)
        self.assertEqual(ingesters[source_type], local_ingest)
