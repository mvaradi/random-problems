def load_sequence(path):
    """
    Simple function to get a sequence from a file that only has one line
    :param path: String; path to the file
    :return: String; a sequence
    """
    try:
        with open(path) as sequence_file:
            return sequence_file.readline().strip()
    except IOError:
        raise Exception('File error')
