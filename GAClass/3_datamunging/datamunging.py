#!/usr/bin/python

#from numpy import *
from numpy import array, dot, arange
from scipy import linalg

X = array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = array([[1], [2], [3], [4]])
#n = inv(dot(X.T, X))
#k = dot(X.T, y)
#coef_ = dot(n, k)

def regression(input, response):
    return dot(linalg.inv(dot(X.T, X)), dot(X.T, y))

if __name__ == "__main__":

    arrayOne = arange(15).reshape(3, 5)
    print arrayOne
