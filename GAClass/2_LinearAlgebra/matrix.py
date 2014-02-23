
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
    #len(matrix[0]) # Use this 4 as Step 1 (number of for loops)
    #matrix_transpose(matrix) #[[8, 1, 7, 0], [9, 4, 8, 6], [4, 4, 8, 0], [0, 7, 2, 1]] Step 2
    #[x for x in vector] #[2, 3, 6, 5]
    list_output = []
    tmatrix = matrix_transpose(matrix)
    for i in range(len(matrix[0])):
        total = 0
        for x in range(len(vector)):
            total = total + vector[x] * tmatrix[i][x]
        list_output.append(total)
    return list_output

def matrix_matrix(matrix1, matrix2):
    pass

#print vector
print "Matrix 1 is: ", matrix1
print "Transposed Matrix 1 is: ", matrix_transpose(matrix1)
print "Matrix to Vector Multiplication: ", matrix_vector(matrix1, vector)
