""" Binary Search """


def binarySearch(mylist, item):
    first = 0
    last = len(mylist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last) // 2
        if mylist[midpoint] == item:
            found = True
        else:
            if item < mylist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


if __name__ == '__main__':
    mylist = [54,26,93,17,77,31,44,55,20]
    print "Original: ", mylist
    print binarySearch(mylist, 26)
    #print binarySearch(mylist, 18)