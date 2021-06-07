"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""
import sys
from rosalind.sequence_manipulation import DNA
from rosalind.file_handling import FileHandler

# Example
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# = 7

fh = FileHandler(path=sys.argv[1])
sequences = fh.load_sequence_pair()
dna = DNA(sequences[0])
print(dna.count_point_mutations(variant_seq=sequences[1]))

