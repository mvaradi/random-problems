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
        with self.assertRaises(Exception):
            FileHandler('missing.txt').load_sequence()

    def test_load_fasta(self):
        with open('tmp.fasta', 'w') as tmp:
            tmp.write('>asd\nFOO\n>bar\nASD')
        seq = FileHandler('tmp.fasta').load_fasta()
        self.assertEqual(seq, {'asd': 'FOO', 'bar': 'ASD'})
        os.system('rm tmp.fasta')

    def test_load_sequence_pair(self):
        os.system('echo FOO > tmp.txt')
        os.system('echo BAR >> tmp.txt')
        seq = FileHandler('tmp.txt').load_sequence_pair()
        self.assertEqual(seq, ('FOO', 'BAR'))
        os.system('rm tmp.txt')

    def test_repr(self):
        fh = FileHandler('path/to/file')
        self.assertEqual(str(fh), 'FileHandler(path="path/to/file")')
