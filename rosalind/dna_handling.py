class DNA(object):
    """
    A class for performing basing transformation on a DNA sequence

    These methods are used to solve problems posted on Rosalind
    """

    def __init__(self, dna_seq):
        self.dna_seq = dna_seq
        self.trans_seq = ''
        self.comp_seq = ''
        self.mapping = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }

    def transcribe_dna(self):
        """
        Replace all the 'T' bases with 'U' bases in a sequence
        :return: None
        """
        self.trans_seq = self.dna_seq.replace('T', 'U')

    def complement_sequence(self):
        for base in self.dna_seq:
            self.comp_seq = self.mapping[base] + self.comp_seq

    def count_bases(self):
        bases = {
            'A': self.dna_seq.count('A'),
            'T': self.dna_seq.count('T'),
            'C': self.dna_seq.count('C'),
            'G': self.dna_seq.count('G')
        }
        return bases


