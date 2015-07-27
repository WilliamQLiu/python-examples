#! /usr/bin/env python
""" Does a string contain all unique characters?  """

import unittest


class UniqueTest(unittest.TestCase):

    def test_bf_no_duplicates(self, myinput='abcde'):
        result = brute_force(myinput)
        self.assertEqual(result, True)

    def test_bf_duplicates(self, myinput='aabcde'):
        result = brute_force(myinput)
        self.assertEqual(result, False)


def brute_force(myinput):
    """
        Get input string, return True if string has all unique characters,
        otherwise return False if a duplicate character exists
    """

    for a in range(len(myinput)-1):
        for b in range(a+1, len(myinput)-1):
            if myinput[a] == myinput[b]:
                return False
            else:
                pass
    return True


if __name__ == '__main__':

    unittest.main()