""" Insertion Sort """

def insertionSort(mylist):
    for index in range(1, len(mylist)):
        print "Index is ", index  # 1, 2, 3, 4, 5, 6, 7, 8; this is the outer loop

        # setup first case (only one item)
        currentvalue = mylist[index]
        position = index

        # this is the inner loop, loops through the sorted list backwards and compares values
        while position > 0 and mylist[position-1] > currentvalue:
            mylist[position] = mylist[position-1]
            position = position - 1

        mylist[position] = currentvalue  # found spot in inner sorted loop to place item

if __name__ == '__main__':
    mylist = [54,26,93,17,77,31,44,55,20]
    print "Original: ", mylist
    insertionSort(mylist)
    print "Insertion Sorted: ", mylist