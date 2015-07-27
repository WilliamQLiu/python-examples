""" Selection Sort """

def selectionSort(mylist):
    for fillslot in range(len(mylist)-1, 0, -1):
        #print fillslot  # backwords (8,7,6,..2,1) b/c other items are already sorted
        positionOfMax = 0
        for i in range(1, fillslot+1):
            if mylist[i] > mylist[positionOfMax]:  # is value greater than value at max
                positionOfMax = i

        # to move the largest value to the largest index, we 'swap' the item
        # currently in the largest index position
        mylist[fillslot], mylist[positionOfMax] = mylist[positionOfMax], mylist[fillslot]


if __name__ == '__main__':
    mylist = [54,26,93,17,77,31,44,55,20]
    print "Original: ", mylist
    selectionSort(mylist)
    print "Selection Sorted: ", mylist