"""
PROBLEM 01 - Transcribing DNA into RNA

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by
replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.

Example input: GATGGAACTTGACTACGTAAATT
Example output: GAUGGAACUUGACUACGUAAAUU
"""

import sys
from rosalind.file_handling import FileHandler
from rosalind.sequence_manipulation import DNA

fh = FileHandler(path=sys.argv[1])
dna = DNA(fh.load_sequence())
dna.transcribe_dna()
print(dna.trans_seq)
