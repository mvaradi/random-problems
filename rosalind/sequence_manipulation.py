class Sequence:
    """
    A class for performing sequence manipulations
    """

    def __init__(self, seq):
        self.seq = seq
        self.comp_seq = ''
        self.alphabet = []
        self.mapping = {}

    def count_bases(self):
        """
        Count the 4 bases in a DNA/RNA sequence
        :return: Dict; the count of the 4 DNA/RNA bases
        """
        count = {}
        for letter in self.alphabet:
            count[letter] = self.seq.count(letter)
        return count

    def count_gc_content(self):
        """
        Count the G/C content of a DNA/RNA sequence
        :return: Float; the ratio of G/C bases in the sequence
        """
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq)

    def count_point_mutations(self, variant_seq):
        """
        Count the number of point mutation between a DNA/RNA sequence and another sequence
        :return: Number; the number of point mutations
        """
        count = 0
        for i in range(len(self.seq)):
            if self.seq[i] != variant_seq[i]:
                count += 1
        return count

    def complement_sequence(self):
        """
        Generate the complement sequence of a DNA/RNA sequence
        :return: None
        """
        for base in self.seq:
            self.comp_seq = self.mapping[base] + self.comp_seq


class DNA(Sequence):
    """
    A class for performing basing transformation on a DNA sequence

    These methods are used to solve problems posted on Rosalind
    """

    def __init__(self, seq):
        super().__init__(seq)
        self.trans_seq = ''
        self.comp_seq = ''
        self.alphabet = ['A', 'T', 'G', 'C']
        self.mapping = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }

    def __repr__(self):
        return f'{type(self).__name__}(seq="{self.seq[0:10]}...")'

    def transcribe_dna(self):
        """
        Replace all the 'T' bases with 'U' bases in a sequence
        :return: None
        """
        self.trans_seq = self.seq.replace('T', 'U')


class RNA(DNA):
    """
    A class for performing sequence manipulations on an RNA sequence
    """

    def __init__(self, seq):
        super().__init__(seq)
        self.comp_seq = ''
        self.protein_seq = ''
        self.alphabet = ['A', 'U', 'G', 'C']
        self.mapping = {
            'A': 'U',
            'U': 'A',
            'G': 'C',
            'C': 'G'
        }
        self.codon_map = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L',
            'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
            'AUG': 'M',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'UAU': 'Y', 'UAC': 'Y',
            'CAU': 'H', 'CAC': 'H',
            'AAU': 'N', 'AAC': 'N',
            'GAU': 'D', 'GAC': 'D',
            'CAA': 'Q', 'CAG': 'Q',
            'AAA': 'K', 'AAG': 'K',
            'GAA': 'E', 'GAG': 'E',
            'UGU': 'C', 'UGC': 'C',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
            'UGG': 'W',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
            'UGA': '', 'UAG': '', 'UAA': ''
        }

    def translate(self):
        """
        Translate an RNA sequence into amino acid sequence using the codon table
        :return: None
        """
        i = 0
        while i < len(self.seq) - 2:
            codon = self.seq[i:i+3]
            if self.codon_map[codon] == '':
                break
            self.protein_seq += self.codon_map[codon]
            i += 3
