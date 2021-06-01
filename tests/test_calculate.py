from unittest import TestCase
from rosalind.calculate import fib_sequence


class TestCalculate(TestCase):
    """
    Test the functions in rosalind.calculate
    """

    def test_fib_sequence(self):
        self.assertEqual(fib_sequence(5, 3), 19)
