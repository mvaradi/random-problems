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

    def test_count_gc_content(self):
        dna = DNA('CGCGCGCGC')
        self.assertEqual(dna.count_gc_content(), 1)
        dna = DNA('AATTCCGG')
        self.assertEqual(dna.count_gc_content(), 0.5)

    def test_count_point_mutations(self):
        dna_seq = 'GAGCCTACTAACGGGAT'
        variant = 'CATCGTAATGACGGCCT'
        dna = DNA(dna_seq=dna_seq)
        self.assertEqual(dna.count_point_mutations(variant), 7)

    def test_repr(self):
        dna = DNA('GAGCCTACTAACGGGAT')
        self.assertEqual(str(dna), 'DNA(dna_seq="GAGCCTACTA...")')
