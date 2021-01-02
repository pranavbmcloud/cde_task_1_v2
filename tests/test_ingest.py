"""Module tests functionalty in ingest.py"""


import unittest
from src.ingest import local_ingest


class TestLocalIngest(unittest.TestCase):
    """Tests local ingest functionality"""
    def test_local_ingest_without_filepath_raises_TypeError(self):
        with self.assertRaises(TypeError):
            local_ingest()