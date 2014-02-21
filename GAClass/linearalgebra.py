""" Linear Algebra - Class 2 """

import sys
import os

vector = [2, 3, 6, 5]
matrix = [[1,3,9,2], [2,4,6,8]]

def if_else_example():
    """ How to use if, elif, else """
    x,y = False, False
    if x:
        print 'apple'
    elif y:
        print 'banana'
    else:
        print 'sandwich'

def while_loop_example():
    """ How to use while loop """
    x = 0
    while True:
        print 'HELLO!'
        x += 1
        if x >=3:
            break

def range_example():
    """ How to use range() """
    for k in range(4):
        print k

def vector_example():
    """ How to use vector and matrix """
    vector = [1, 2, 3]
    print "Vector:", vector #[1, 2, 3]

    matrix = [ [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12] ]
    print "Matrix:", matrix #[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print "Matrix[0]:", matrix[0] #[1, 2, 3, 4]
    print "Matrix[0][2]:", matrix[0][2] #3

def list_comprehension_example():
    """ How to use list comprehension, long way and short 
    Multiply each value within a vector by a value, 
    not repeat the vector 3 times """
    vector = [1, 2, 3]
    
    # Long way
    l=[]
    for x in vector:
        l.append(x*3)
    print l #[3, 6, 9]

    # Short way
    res = [x*3 for x in vector]
    print res #[3, 6, 9]

    # Another way
    l = [1, 2, 3]
    for i, x in enumerate(vector):
        l[i] = l[i] * 3
    print l #[3, 6, 9]

def vector_multiply(vector, val):
    """ Take a vector and multiply by val across entire vector"""
    return [x*val for x in vector]

def matrix_transpose(matrix):
    """ Take a matrix and transpose it (flip it onto its side) """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    # rows become columns
    # Example:
    # [2 1 0 ]           [2 0]
    # [0 3 0 ]  becomes  [1 3] 
    #                    [0 0]

if __name__ =='__main__':
    #if_else_example()
    #while_loop_example()
    #range_example()
    #vector_example()
    #list_comprehension_example()
    print vector_multiply(vector, 5) #[10, 15, 30, 25]
    print matrix_transpose(matrix)

