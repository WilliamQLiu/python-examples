
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
    return [x*val for x in vector]

def matrix_transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def vector_matrix_multiplication(vector, matrix):
    matrix = matrix_transpose(matrix)
    if len(matrix) != len(vector):
        return None
    res = [[matrix[j][i]*vector[j] for j in range(len(matrix))]for i in range(len(matrix[0]))]
    for i in range(len(res)):
        val = 0
        for j in res[i]:
            val += j
        res[i] = val
    return res

def matrix_matrix_multiplication(m1, m2):
    m2 = matrix_transpose(m2)
    return [vector_matrix_multiplication(i, m1) for i in m2]

print vector
print matrix
