"""
PROBLEM 02 - Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

import sys
from rosalind.file_handling import load_sequence
from rosalind.dna_handling import DNA

dna = DNA(load_sequence(sys.argv[1]))
dna.complement_sequence()
print(dna.comp_seq)
