"""Module tests functionalty in write.py"""


import unittest, os
from src.write import simple_writer, list_writer
from src.file_type import get_data_type


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

    def tearDown(self) -> None:
        import os
        os.remove(self.output_file_name)


class TestWritelistOfDicts(unittest.TestCase):
    """Tests write of list of dicts"""
    def setUp(self) -> None:
        self.list_of_dicts = [
            {
                'key1': 'value1', 'key2': 'value2'
            },
            {
                'key3': 'value3', 'key4': 'value4'
            },
            {
                'key5': 'value5', 'key6': 'value6'
            }
        ]
        self.expected_data =[
            'key1\tkey2\n',
            'value1\tvalue2\n',
            'key3\tkey4\n',
            'value3\tvalue4\n',
            'key5\tkey6\n',
            'value5\tvalue6\n'
        ]
        self.output_file = "./tests/list_writer_output.txt"
        list_writer(self.list_of_dicts, self.output_file)
        with open(self.output_file, 'r') as f:
            self.written_data = f.readlines()

    def test_write_list_of_dicts(self):
        self.assertEqual(self.written_data, self.expected_data)

    def tearDown(self) -> None:
        import os
        os.remove(self.output_file)


class TestWriters(unittest.TestCase):
    """Tests writers returned based on Data Type"""
    def test_writers_returns_list_writer_for_json(self):
        """List writer is required as this handles multiple blocks of json"""
        testing_file = "./tests/json_testing_sample.json"
        file_type = get_data_type(testing_file)
        self.assertEqual(writers[file_type], list_writer)
