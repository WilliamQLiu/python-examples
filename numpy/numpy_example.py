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
import numpy.linalg as LA  # Linear Algebra


def numpy_overview():
    """ NumPy's main object is the homogeneous multidimensional array.
    It is a table of elements, all of the same type, indexed by a tuple
    of positive integers.  Dimensions are called 'axes', the number of
    axes is 'rank'. """
    print "NUMPY OVERVIEW"

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

    print my_array.dtype  # int32
    # an object describing the type of elements in the array

    print my_array.dtype.name  # int32

    print my_array.itemsize  # 8
    # the size in bytes of each element of the array


def create_arrays():
    """
        Can create an array similar to a Python list using the array function
        NumPy arrays are different than Python lists in that the data type must
        be the same (can't have str, ints in the same array)
        Good for math operations
    """
    print "CREATE ARRAYS"
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
    print "PRINT ARRAYS"
    a = np.arange(6)  # 1 Dimensional Array
    b = np.linspace(0, 5, num=6)  # 6 evenly spaced numbers bet 0 and 5 inclu.
    c = np.arange(12).reshape(4, 3)  # 2 Dimensional Array
    d = np.arange(24).reshape(2, 3, 4)  # 3 Dimensional Array

    np.set_printoptions(precision=8, threshold='nan', linewidth=75,
                        suppress=False)
    # precision means number of digits for floating point (default 8)  [ 1.1235]
    # threshold means number of array elements which trigger summarization [0 1 2 ..., 7 8 9]
    # linewdith means number of chars per line for inserting line breaks
    # suppress printing of small float values using scientific notation

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


def basic_operations():
    """ Arithmetic operators on arrays apply elementwise.
        Say you have array [1,2,3]*2.
        NumPy result would be [2,4,6]
        Python list would be [1,2,3,1,2,3]
     """
    print "BASIC OPERATIONS"

    ### Elementwise Example
    a = np.array([20,30,40,50])
    b = np.arange(4)  # array([0,1,2,3])
    c = a-b  # elementwise subtraction
    print c  # which translates to 20-0, 30-1, 40-2, 50-3

    print b**2  # b squared is: array([0, 1, 4, 9])

    ### Operator and Matrix Examples
    d = np.array( [[1,1],
                   [0,1]] )
    e = np.array( [[2,0],
                   [3,4]] )
    f = d * e  # Elementwise (Note: * operator is elementwise, not Matrix)
    print f
    # [[2 0]   # 1*2, 1*0
    #  [0 4]]  # 0*3, 1*4

    g = np.dot(d,e)  # Matrix-Matrix product (col of d must equal row of e)
    print g
    # [[5 4]   # 1*2+1*3=5, 1*0+1*4=4
    #  [3 4]]  # 0*2+1*3=3, 0*3+1*4=4

    ### Modify existing array instead of creating a new one with +=, *=, etc
    h = np.ones((2,3), dtype=int)  # Just create an array of value = 1
    i = np.random.random((2,3))
    h *= 3
    print h  # modifies array in place
    #  [[3, 3, 3]
    #   [3, 3, 3]]

    i += h
    print i
    #  [[ 3.69092703,  3.8324276 ,  3.0114541 ],
    #   [ 3.18679111,  3.3039349 ,  3.37600289]]


def copy_arrays():
    """ NumPy is so efficient that it doesn't copy an array (it works off
        a reference) unless you explicitly say to copy """

    a = np.array([0, 1, 2, 3, 4, 5])  # [0, 1, 2, 3, 4, 5]
    b = a.reshape((3,2))
    print b
    # [[0,1],
    #  [2,3],
    #  [4,5]]
    b[1][0] = 77
    print b
    # [[0,1],
    #  [77,3],
    #  [4,5]]
    print a # [0, 1, 77, 3, 4, 5]  # Change in b is immediately reflected in a
    c = a.reshape((3,2)).copy()  # Explicitly copy object to not reference
    c[0][0] = -99
    print c
    # [[-99,1],
    #  [77,3],
    #  [4,5]]
    print a  # [0, 1, 77, 3, 4, 5]


def describe_array():
    """ Functions to describe the data """
    j = np.random.random((2,3))
    # [[ 3.96657209, 3.48986127, 3.29158525]
    #  [ 3.31593393, 3.08371726, 3.149423]]
    print j.sum()  # 20.2970927837
    print j.min()  # 3.08371725942
    print j.max()  # 3.96657208502

    ### slice by col, row and cumulative sum across col, row
    print j.sum(axis=0)  # sum of each column
    print j.min(axis=1)  # min of each row
    print j.cumsum(axis=0)  # cumulative sum along each col
    print j.cumsum(axis=1)  # cumulative sum along each row


def index_slice_iterate():
    """ Index, Slice, and Iterate over one-dimensional and multidimensional
    arrays """

    ### One-dimensional Arrays
    a = np.arange(10)**3
    print a  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

    print a[2]  # 8, select by index
    print a[2:5]  # [8, 27, 64], select by range of indexes
    a[:6:2] = -10  # from start to index 6, exclusive, set every 2nd ele to -10
    print a  # [-10, 1, -10, 27, -10, 125, 216, 343, 512, 729]

    ### Multidiemnsional Arrays
    b = np.array([[0, 1, 2, 3,],
                  [10, 11, 12, 13],
                  [20, 21, 22, 23],
                  [30, 31, 32, 33],
                  [40, 41, 42, 43]])
    print b[2,3]  # 23, selects row, column (remember it starts with 0)
    print b[0:5,1]  # [1, 11, 21, 31, 41]  every row in the second col
    print b[1:3,]  # every col in the 2nd and 3rd row
    # [[10 11 12 13],
    #  [20 21 22 23]]

    ### Iterating over multidimensional arrays is with respect to first axis
    for row in b:
        print row
    # [0, 1, 2, 3]
    # [10, 11, 12, 13]
    # [20, 21, 22, 23]
    # [30, 31, 32, 33]
    # [40, 41, 42, 43]

    ### If you want to perform an operation on each element, use 'flat'
    for item in b.flat:
        print item,  # without comma, goes to next line
    #0, 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33, 40, 41, 42, 43


def shape_manipulation():
    """ An array can be reshaped along each axis """
    a = np.floor(10 * np.random.random((3,4)))
    print a
    #[[0, 8, 4, 8],
    # [4, 9, 7, 0],
    # [6, 4, 0, 2]]
    print a.shape # 3, 4

    ### Flatten with unravel
    print a.ravel()  # [0, 8, 4, 8, 4, 9, 7, 0, 6, 4, 0, 2]

    ### Reshape the rows and cols with shape
    a.shape = (6,2)  # a -1 value will automatically calculate dimensions
    print a
    # [[0, 8],
    #  [4, 8],
    #  [4, 9],
    #  [7, 0],
    #  [6, 4],
    #  [0, 2]]

    ### Transpose
    print a.transpose()  # basically flip over
    # [[0, 4, 4, 7, 6, 0],
    #  [8, 8, 9, 0, 4, 2]]


def stack_unstack():
    """ Arrays can be stacked together along different axes """

    ### One dimensional Arrays use vstack and column_stack
    a = np.array([0, 1, 2, 3])
    b = np.array([4, 5, 6, 7])

    print np.vstack((a, b))  # vertically stack one array on top of other
    # [[0, 1, 2, 3],
    #  [4, 5, 6, 7]]

    print np.column_stack((a, b))  # horizontally stack one array next to other
    # [[0, 4],
    #  [1, 5],
    #  [2, 6],
    #  [3, 7]]

    ### Two dimensional Arrays use vstack and hstack
    a = np.array([[0, 1],
                  [2, 3]])
    b = np.array([[4, 5],
                  [6, 7]])

    print np.vstack((a,b))  # vertically stack one array on top of other
    # [[0, 1],
    #  [2, 3],
    #  [4, 5],
    #  [6, 7]]

    print np.hstack((a,b))  # horizontally stack one array next to other
    # [[0, 1, 4, 5],
    #  [2, 3, 6, 7]]


def linear_algebra():
    """ Use the `numpy.linalg` library to do Linear Algebra
        For a reference on math, see 'Linear Algebra explained in four pages'
        http://minireference.com/static/tutorials/linear_algebra_in_4_pages.pdf
    """

    ### Setup two vectors
    x = np.array([1, 2, 3, 4])
    y = np.array([5, 6, 7, 8])

    ### Vector Operations include addition, subtraction, scaling, norm (length),
    # dot product, and cross product
    print np.vdot(x, y)  # Dot product of two vectors


    ### Setup two arrays / matrices
    a = np.array([[1, 2],
                  [3, 9]])
    b = np.array([[2, 4],
                  [5, 6]])


    ### Dot Product of two arrays
    print np.dot(a, b)


    ### Solving system of equations (i.e. 2 different equations with x and y)
    print LA.solve(a, b)


    ### Inverse of a matrix undoes the effects of the Matrix
    # The matrix multipled by the inverse matrix returns the
    # 'identity matrix' (ones on the diagonal and zeroes everywhere else);
    # identity matrix is useful for getting rid of the matrix in some equation
    print LA.inv(a)  # return inverse of the matrix
    print "\n"


    ### Determinant of a matrix is a special way to combine the entries of a
    # matrix that serves to check if matrix is invertible (!=0) or not (=0)
    print LA.det(a)  # returns the determinant of the array
    print "\n"  # e.g. 3, means that it is invertible


    ### Eigenvectors is a special set of input vectors for which the action of
    # the matrix is described as simple 'scaling'.  When a matrix is multiplied
    # by one of its eigenvectors, the output is the same eigenvector multipled
    # by a constant (that constant is the 'eigenvalue' of the matrix)
    print LA.eigvals(a)  # comput the eigenvalues of a general matrix
    print "\n"
    print LA.eigvalsh(a)  # Comput the eigenvalues of a Hermitian or real symmetric matrix
    print "\n"
    print LA.eig(a)  # return the eigenvalues for a square matrix
    print "\n"
    print LA.eigh(a)  # return the eigenvalues or eigenvectors of a Hermitian or symmetric matrix
    print "\n"


if __name__ == '__main__':
    #numpy_overview()  # basics of getting array dim, shape, size, items
    #create_arrays()  # how to create an array, specify type and dimensions
    copy_arrays()
    #print_arrays()  # show different print options for numbers in array
    #basic_operations()  # doing math on numpy arrays
    #describe_array()  # describe array: min, max, sum, cumsum
    #index_slice_iterate()  # how to index, slice, iterate over arrays
    #shape_manipulation()  # how to change shape of arrays
    #stack_unstack()  # stack or unstack arrays together along different axes
    #linear_algebra()  # numpy.linalg for Linear Algebra calculations