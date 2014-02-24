
import sys
import os

vector = [2, 3, 6, 5]

matrix = [[1,3,9,2], [2,4,6,8]]

matrix1 = [[8,9,4,0],
          [1,4,4,7],
          [7,8,8,2],
          [0,6,0,1]]
matrix2 = [[2,5,2,6],
          [4,4,6,3],
          [4,5,5,1],
          [2,4,6,8]]

# Matrix 3 has an incompatible matrix size for vector of size 4
matrix3 = [[8,9,4,0,7],
          [1,4,4,7,7],
          [7,8,8,2,3],
          [0,6,0,1,4]]

def vector_multiply(vector, val):
    """ Multiply val across all of vector """
    return [x*val for x in vector]

def matrix_transpose(matrix):
    """ Transpose Matrix (flip matrix to side) - row to columns """
    # Same as:
    #transposed = []
    #for i in range(len(matrix[0])):
    #    transposed.append([row[i] for row in matrix])
    #print transposed

    # Same as:
    #transposed = []
    #for i in range(len(matrix[0])):
    #    transposed_row = []
    #    for row in matrix:
    #        transposed_row.append(row[i])
    #    transposed.append(transposed_row)
    #print transposed
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def matrix_vector(matrix, vector):
    """ Vector * matrix, transpose matrix so can multiply list """
    #len(matrix[0]) # Use this 4 as Step 1 (number of for loops)
    #matrix_transpose(matrix) #[[8, 1, 7, 0], [9, 4, 8, 6], [4, 4, 8, 0], [0, 7, 2, 1]] Step 2
    #[x for x in vector] #[2, 3, 6, 5]

    assert (len(matrix[0]) == len(vector)), "Vector length must match mat col"
        #print "Length of Vector is: ", len(vector)
        #print "Col Length of Matrix is: ", len(matrix[0])
    transposed_matrix = matrix_transpose(matrix)
    my_output = []
    for row in range(len(matrix[0])):
        total = 0
        for index in range(len(vector)):
            total = total + vector[index] * transposed_matrix[row][index]
        my_output.append(total)
    return my_output

def matrix_matrix(matrix1, matrix2):
    """ Multiply 2 matrix, transpose matrix2, then vector * matrix formula """
    transposed_matrix = matrix_transpose(matrix2)
    my_output = []
    for row in range(len(matrix2)):
        my_output.append(matrix_vector(matrix1, transposed_matrix[row]))
    return my_output

def identity_matrix(matrix):
    """ Identity Matrix must be square, returns 1 on same x and y, else 0 """
    size = len(matrix[0])
    my_output = []
    for x in range(size):
        my_list=[]
        for y in range(size):
            if x == y:
                my_list.append(1)
            else:
                my_list.append(0)
        my_output.append(my_list)
    return my_output

print "Vector is: ", vector
print "Matrix 1 is: ", matrix1
print "Transposed Matrix 1 is: ", matrix_transpose(matrix1)
print "Matrix to Vector Multiplication: ", matrix_vector(matrix1, vector)
print "Matrix 2 is: ", matrix2
print "Matrix1 to Matrix2 Multiplication: ", matrix_matrix(matrix1, matrix2)
print "Creating Identity Matrix for Matrix1: ", identity_matrix(matrix1)
print "Matrix1 times Identity Matrix: ", \
    matrix_matrix(matrix1, identity_matrix(matrix1))
