""" Python 3 implementation of a quickselect algorithm """
from typing import List
import unittest
import random


class Solution:

    def quickselect(self, items, item_index):
        if items is None or len(items) < 1:
            return None

        if item_index < 0 or item_index > len(items) - 1:
            raise IndexError()

        return self.select(items, 0, len(items) - 1, item_index)

    def select(self, lst, l, r, index):
        # base case
        if r == l:
            return lst[l]

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to beginning of list
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]

        # recursively partition one side only
        if index == i:
            return lst[i]
        elif index < i:
            return self.select(lst, l, i-1, index)
        else:
            return self.select(lst, i+1, r, index)


class SolutionTest(unittest.TestCase):

    def test_quickselect(self):
        s = Solution()
        response = s.quickselect([12, 2, 4, 3, 5], 2)
        assert response == 4

        response = s.quickselect([12, 2, 4, 3, 5], 0)
        assert response == 2




if __name__ == '__main__':
    unittest.main()
