import os
from unittest import TestCase
from rosalind.file_handling import FileHandler


class TestFileHandler(TestCase):
    """
    Test the file handling functions
    """

    def test_load_sequence(self):
        os.system('echo FOO > tmp.txt')
        seq = FileHandler('tmp.txt').load_sequence()
        self.assertEqual(seq, 'FOO')
        os.system('rm tmp.txt')

    def test_load_sequence_no_file(self):
        with self.assertRaises(Exception) as context:
            FileHandler('missing.txt').load_sequence()
