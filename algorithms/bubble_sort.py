""" Bubble Sort """

def bubbleSort(mylist):
    for passnum in range(len(mylist)-1, 0, -1):
        #print passnum  # backwords (8,7,6,..2,1) b/c other items are already sorted
        for i in range(passnum):
            if mylist > mylist[i+1]:  # compare neighbors
                mylist, mylist[i+1] = mylist[i+1], mylist  # swap


if __name__ == '__main__':
    mylist = [54,26,93,17,77,31,44,55,20]
    print "Original: ", mylist
    bubbleSort(mylist)
    print "Bubble Sorted: ", mylist