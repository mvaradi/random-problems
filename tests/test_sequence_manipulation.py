from unittest import TestCase
from rosalind.sequence_manipulation import DNA


class TestDNAHandling(TestCase):
    """
    Testing the methods of the DNA class
    """

    def test_transcribe_dna(self):
        dna = DNA('GATGGAACTTGACTACGTAAATT')
        dna.transcribe_dna()
        self.assertEqual(dna.trans_seq, 'GAUGGAACUUGACUACGUAAAUU')

    def test_complement_sequence(self):
        dna = DNA('AAAACCCGGT')
        dna.complement_sequence()
        self.assertEqual(dna.comp_seq, 'ACCGGGTTTT')

    def test_count_bases(self):
        dna = DNA('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        bases = dna.count_bases()
        self.assertEqual(bases['A'], 20)
        self.assertEqual(bases['C'], 12)
        self.assertEqual(bases['G'], 17)
        self.assertEqual(bases['T'], 21)