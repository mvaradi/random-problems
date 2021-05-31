import os
from unittest import TestCase
from rosalind.file_handling import load_sequence


class TestLoadSequence(TestCase):
    """
    Test the file handling functions
    """

    def test_load_sequence(self):
        os.system('echo FOO > tmp.txt')
        seq = load_sequence('tmp.txt')
        self.assertEqual(seq, 'FOO')
        os.system('rm tmp.txt')

    def test_load_sequence_no_file(self):
        with self.assertRaises(Exception) as context:
            load_sequence('missing.txt')
