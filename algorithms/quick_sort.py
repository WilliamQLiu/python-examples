""" Quick Sort in Python3 """
import pdb


def quickSort(mylist):
    quickSortHelper(mylist, 0, len(mylist)-1)

def quickSortHelper(mylist, first, last):
    if first < last:
        splitpoint = partition(mylist, first, last)

        quickSortHelper(mylist, first, splitpoint-1)
        quickSortHelper(mylist, splitpoint+1, last)

def partition(mylist, first, last):
    #import pdb; pdb.set_trace()
    pivotvalue = mylist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and mylist[leftmark] <= pivotvalue:
            leftmark += 1

        while mylist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            mylist[leftmark], mylist[rightmark] = mylist[rightmark], mylist[leftmark]

    mylist[first], mylist[rightmark] = mylist[rightmark], mylist[first]

    return rightmark


if __name__ == '__main__':
    mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original: ", mylist)
    quickSort(mylist)
    print("Quick Sorted: ", mylist)
