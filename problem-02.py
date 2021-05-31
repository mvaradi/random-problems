class ComplementedDNA(object):
    """
    In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

    The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s.
    """


    def __init__(self, dna):
        self.dna_sequence = dna
        self.complemented_sequence = ''
        self.mapping = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }

    def complement_sequence(self):
        for base in self.dna_sequence:
            self.complemented_sequence = self.mapping[base] + self.complemented_sequence


"""
Testing with short example sequence
"""
# cdna = ComplementedDNA('AAAACCCGGT')
# cdna.complement_sequence()
# print(cdna.complemented_sequence)
# Expected: ACCGGGTTTT

"""
Running with file
"""
try:
    with open('rosalind_revc.txt') as dna_sequence_file:
        dna_sequence = dna_sequence_file.readline()
        cdna = ComplementedDNA(dna_sequence)
        cdna.complement_sequence()
        print(cdna.complemented_sequence)
except IOError as err:
    print('Error: ' % err)

"""
Notes:

This would also work: print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))

Or even in bash: rev r.txt | tr ATCG TAGC

Or with BioPython:
from Bio.Seq import Seq

file = open("rosalind2.txt", "r")
s = file.read()
seq = Seq(s)
seq.reverse_complement()
print seq.reverse_complement()
"""

