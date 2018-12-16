""" Quick Sort in Python3
Quick sort uses divide and conquer to gain the same advantages as merge sort,
with the benefit of using less storage, but at the cost of a worse worst case runtime
O(n^2) if the pivot values are bad.
"""
import pdb
from typing import List


def quickSort(mylist):
    """ Initialize our recursive function """
    quickSortHelper(mylist, 0, len(mylist)-1)

def quickSortHelper(mylist, first, last):
    """ Recursive function to split up """
    if first < last:  # check if need to sort still

        splitpoint = partition(mylist, first, last)

        # now that we know our splitpoint, we can then recursively run quicksort on the list's bottom half and top half
        quickSortHelper(mylist, first, splitpoint-1)
        quickSortHelper(mylist, splitpoint+1, last)

def partition(mylist, first, last):
    """ Partition Process, made up of:
    * Pick a pivot value (i.e. what we'll compare our unsorted numbers to)
    Based off this value, we'll compare our unsorted values and either move
    our items to the left of the pivot or to the right of the pivot.
    * """
    pivotvalue = mylist[first]  # get the first value as pivotvalue

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        # Go from leftmost side onwards (to right) and try to find a value
        # that is greater than the pivot value (i.e. left side of pivot should be
        # smaller values than pivot value, if we found one that is greater, we
        # stop at leftmark, saying we need to do a swap to the right side)
        while leftmark <= rightmark and mylist[leftmark] <= pivotvalue:
            leftmark += 1

        # Go from rightmost side inwards (to left) and try to find a value
        # that is less than the pivot value (i.e. right side of pivot should be
        # greater values than pivot value, if we found one that is smaller, we
        # stop at rightmark, saying we need to do a swap to the left side)
        while rightmark >= leftmark and mylist[rightmark] >= pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True  # we're done sorting through this list because we've crossed
        else:
            # we have a swap between a value in the left list and a value in the right list
            mylist[leftmark], mylist[rightmark] = mylist[rightmark], mylist[leftmark]

    # Once rightmark is less than leftmark, then rightmark is now the split point.
    # That means what we picked as the pivot value can now be exchanged with the 
    # contents of the split point and the pivot value is now in the correct place
    # Note: remember that our pivot value was the first value in our list
    mylist[first], mylist[rightmark] = mylist[rightmark], mylist[first]

    return rightmark


if __name__ == '__main__':
    mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original: ", mylist)
    quickSort(mylist)
    print("Quick Sorted: ", mylist)
