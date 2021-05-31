"""
PROBLEM 01 - Counting DNA Nucleotides

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a
string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G',
and 'T' occur in s.
"""

import sys
from rosalind.file_handling import load_sequence
from rosalind.dna_handling import DNA

dna = DNA(load_sequence(sys.argv[1]))
bases = dna.count_bases()
print('%i %i %i %i' % (
    bases['A'],
    bases['C'],
    bases['G'],
    bases['T']
))