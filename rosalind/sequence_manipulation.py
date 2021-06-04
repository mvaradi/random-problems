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
        """
        Generate the complement sequence of a DNA sequence
        :return: None
        """
        for base in self.dna_seq:
            self.comp_seq = self.mapping[base] + self.comp_seq

    def count_bases(self):
        """
        Count the 4 bases in a DNA sequence
        :return: Dict
        """
        bases = {
            'A': self.dna_seq.count('A'),
            'T': self.dna_seq.count('T'),
            'C': self.dna_seq.count('C'),
            'G': self.dna_seq.count('G')
        }
        return bases

    def count_gc_content(self):
        """
        Count the G/C content of a DNA sequence
        :return: Float
        """
        return (self.dna_seq.count('G') + self.dna_seq.count('C')) / len(self.dna_seq)

    def count_point_mutations(self, variant_seq):
        """
        Count the number of point mutation between a DNA sequence and another sequence
        :return: Number; the number of point mutations
        """
        count = 0
        for i in range(len(self.dna_seq)):
            if self.dna_seq[i] != variant_seq[i]:
                count += 1
        return count



