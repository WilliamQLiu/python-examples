"""
    Permutation Check - Given two strings, write a method to decide if one is
    a permutation of the other
"""

import unittest


class PermuteTest(unittest.TestCase):
    def test_permute_pass(self, input_a='abcdefgh', input_b='ghfeabcd'):
        result = permute(input_a, input_b)
        self.assertEqual(result, True)

    def test_permute_fail(self, input_a='abcdefgh', input_b='xhfeabcd'):
        result = permute(input_a, input_b)
        self.assertEqual(result, False)


def permute(input_a, input_b):
    list_a = list(input_a)
    list_b = list(input_b)

    list_a.sort()
    list_b.sort()

    if list_a == list_b:
        return True
    else:
        return False


if __name__ == '__main__':

    unittest.main()
