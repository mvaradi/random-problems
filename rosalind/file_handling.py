class FileHandler():
    """
    This class handles input files in various formats
    """

    def __init__(self, path):
         self.path = path
         self.input_file = None
         self.data = None

    def __repr__(self):
        return f'{type(self).__name__}(path="{self.path}")'

    def _open_file(self):
        """"
        Open a file or raise error
        :return: None;
        """
        try:
            self.input_file = open(self.path)
        except IOError:
            raise Exception('File error')

    def _close_file(self):
        """
        Close a file
        :return: None;
        """
        self.input_file.close()

    def load_sequence(self):
        """
        Get a sequence from a file that only has one line
        :return: String; a sequence
        """
        self._open_file()
        data = self.input_file.readline().strip()
        self._close_file()
        return data

    def load_fasta(self):
        """
        Get all the sequences and their identifiers from a fasta file
        :return: Dict; {identifier: sequence}
        """
        self._open_file()
        data = {}
        identifier = None
        for line in self.input_file:
            if line.startswith('>'):
                identifier = line.split('>')[1].strip()
                data[identifier] = ''
            else:
                data[identifier] += line.strip()
        self._close_file()
        return data

    def load_sequence_pair(self):
        """
        Get a sequence from a file that only has one line
        :return: Tuple; two sequences
        """
        self._open_file()
        seq1 = self.input_file.readline().strip()
        seq2 = self.input_file.readline().strip()
        self._close_file()
        return seq1, seq2