class FileHandler():
    """
    This class handles input files in various formats
    """

    def __init__(self, path):
         self.path = path
         self.input_file = None
         self.data = None

    def __repr__(self):
        return f'Opened {self.path}'

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
        """
        self.input_file.close()

    def load_sequence(self):
        """
        Simple function to get a sequence from a file that only has one line
        :param path: String; path to the file
        :return: String; a sequence
        """
        self._open_file()
        data = self.input_file.readline().strip()
        self._close_file()
        return data
