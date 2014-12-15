"""
    NumPy is the fundamental package for scientific computing in Python.
    It provides a multidimensional array object, various derived objects
    (e.g. matrices), and an assortment of routines for fast operations
    on arrays including linear algebra, statistical operations, etc.

    At the core is the 'ndarray' object.  This encapsulates n-dimensional
    arrays with many operations that have great performance (pre-compiled C) w/
    * Vectoriazation - absence of any explicit looping ,indexing, etc.
      Removes lots of for loops, is easier to read and debug, more like math
    * Broadcasting - The implicit element-by-element behavior of operations
      How to treat arrays with different shapes during arithmetic operations

    Reference http://docs.scipy.org/doc/numpy/reference/index.html#module-numpy

    Tutorial: http://wiki.scipy.org/Tentative_NumPy_Tutorial
    Functions: http://wiki.scipy.org/Numpy_Example_List

"""

import numpy as np


def numpy_basics():
    """ NumPy's main object is the homogeneous multidimensional array.
    It is a table of elements, all of the same type, indexed by a tuple
    of positive integers.  Dimensions are called 'axes', the number of
    axes is 'rank'. """

    my_array = np.arange(15).reshape(3, 5)

    print my_array
    # [[ 0  1  2  3  4]
    # [ 5  6  7  8  9]
    # [10 11 12 13 14]]

    print type(my_array)  # <type 'numpy.ndarray'>

    print my_array.ndim  # 2
    # of axes (dimensions) of array

    print my_array.shape  # (3, 5)
    # dimensions of the array as a tuple; (n,m) is matrix n rows and m columns

    print my_array.size  # 15
    # total number of elements in the array

    print my_array.dtype  # int64
    # an object describing the type of elements in the array

    print my_array.itemsize  # 8
    # the size in bytes of each element of the array


def create_arrays():
    """ Can create an array using a Python list with the array function """
    a = np.array([2,3,4])  # 1 Dimensional
    b = np.array([[1.5, 2., 3.],  # 2 Dimensional
                 [4., 5., 6.]])
    c = np.array([10, 20, 30], dtype='int16')  # Can specify data type

    print a
    # [2 3 4]

    print b
    # [[ 1.5  2.   3. ]
    # [ 4.   5.   6. ]]

    print c
    # [10 20 30]


def print_arrays():
    """ How to display arrays """
    a = np.arange(6)  # 1 Dimensional Array
    b = np.linspace(0, 5, num=6)  # 6 evenly spaced numbers bet 0 and 5 inclu.
    c = np.arange(12).reshape(4, 3)  # 2 Dimensional Array
    d = np.arange(24).reshape(2, 3, 4)  # 3 Dimensional Array

    np.set_printoptions(threshold='nan')  # No threshold

    print a
    # [0 1 2 3 4 5]

    print b
    # [ 0.  1.  2.  3.  4.  5.]

    print c
    # [[ 0  1  2]
    # [ 3  4  5]
    # [ 6  7  8]
    # [ 9 10 11]]

    print d
    # [[[ 0  1  2  3]
    # [ 4  5  6  7]
    # [ 8  9 10 11]]

    # [[12 13 14 15]
    # [16 17 18 19]
    # [20 21 22 23]]]


if __name__ == '__main__':
    #numpy_basics()
    #create_arrays()
    print_arrays()
