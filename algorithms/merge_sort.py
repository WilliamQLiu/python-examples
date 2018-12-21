""" Merge Sort """


def mergeSort(mylist):
    print("Splitting", mylist)

    if len(mylist) > 1:
        mid = len(mylist) // 2
        lefthalf = mylist[:mid]
        print("Left half ", lefthalf)
        righthalf = mylist[mid:]
        print("Right half ", righthalf)

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # below code merges the two smaller sorted lists to larger sorted list
        i = 0  # left half index
        j = 0  # right half index
        k = 0  # main / large sorted list

        while i < len(lefthalf) and j < len(righthalf):

            # take the smallest value from either left or right half
            if lefthalf[i] < righthalf[j]:
                mylist[k] = lefthalf[i]  # smaller value on lefthalf
                i += 1
            else:
                mylist[k] = righthalf[j]  # smaller value on righthalf
                j += 1
            k += 1

        # insert remaining values from lefthalf
        while i < len(lefthalf):
            mylist[k] = lefthalf[i]
            i += 1
            k += 1

        # insert remaining values from righthalf
        while j < len(righthalf):
            mylist[k] = righthalf[j]
            j += 1
            k += 1

    print("Merging", mylist)


if __name__ == '__main__':
    mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original: ", mylist)
    mergeSort(mylist)
    print("Merge Sorted: ", mylist)
