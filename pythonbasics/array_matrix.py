""" NumPy provides the most important data types for data analysis, including:
    Arrays (can have 1, 2, 3+ dimensions) - base data type in NumPy, reliable
      Arrays can be quickly treated as matrix using 'asmatrix' or 'mat'
    Matrices always have 2 dimensions

    Standard mathematical operators on arrays operate element-by-element, but
    not for matrices where multiplication follows the rules of linear algebra
    using 'dot'.  The function 'multiply' can be used on two matrices for
    element-by-element operations.
"""
import numpy


def single_array_example():
    ''' Single dimension array '''
    x = [0.0, 1, 2, 3, 4]
    y = numpy.array(x)
    #x = numpy.array([0.0, 1, 2, 3, 4])
    print y, " is an array"
    print type(y)
    # [ 0.  1.  2.  3.  4.]  is an array
    # <type 'numpy.ndarray'>


def multiple_arrays_example():
    ''' Two (or more) dimensional arrays are initialized using nested lists '''
    y = numpy.array([[0.0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9]])
    print numpy.shape(y)  # (2, 5)

    y = numpy.array([[1,2],
                     [3,4],
                     [5,6],
                     [7,8]])
    print numpy.shape(y)  # (4, 2)

    z = numpy.array(y, dtype='float64')  # Force NumPy type dtype


def matrix_example():
    ''' Matrices are a subset of arrays and are very similar except they always
        have 2 dimensions and follow rules of linear algebra for multiplication
    '''
    x = [0.0, 1, 2, 3, 4]  # Any float makes this all float
    y = numpy.array(x)
    print type(y)  # <type 'numpy.ndarray'>
    print y * y  # Element-by-element calculation
    # [  0.   1.   4.   9.  16.]

    z = numpy.asmatrix(x)
    print type(z)  # <class 'numpy.matrixlib.defmatrix.matrix'>
    print z  # [[ 0.  1.  2.  3.  4.]]
    #print z * z  # Can't do this, returns ValueError: matrices are not aligned
    print numpy.ndim(z)  # 2  # Size of a matrix is always 2 dimensional


def array_selection():
    ''' Pure scalar selection is the simplest method to select elements from an
        array '''

    # 1 dimensional array [i]
    x = numpy.array([10.0, 20.0, 30.0, 40.0, 50.0])
    print x[0]  # 10.0

    # 2 dimensional array [i, j] for index i and j row
    x = numpy.array([[10.0, 20.0, 30.0],[40.0, 50.0, 60.0]])
    print x[1,2]  # 60.0


def array_slicing():
    ''' Arrays are sliced using the syntax [:,:,...,:] where the number of
        dimensions of the arrays determines the size of the slice.  E.g.
        Slice notation a:b:s will select every sth element where i satisfies
        a <= i < b '''
    # Shorthand notations
    # : and :: are the same as 0:n:1 where n is the length of the array or list
    # a: and a:n are the same as a:n:1
    # :b is the same as 0:b:1
    # ::s is the same as 0:n:s where n is the length of the array or list

    x = numpy.array([10, 20, 30, 40, 50])

    # 1 Dimensional Arrays

    y = x[:]  # Returns entire array
    print y  # [10 20 30 40 50]

    y = x[:2]  # Returns first two elements (index 0 and 1)
    print y  # [10 20]

    y = x[1::2]  # Returns from 1st element on for every 2nd element
    print y  # [20 40]

    # 2 Dimensional Arrays - first dimension is row(s), second is column(s)
    # Syntax of z[a:b, c:d] is same as z[a:b,:][:,c:d] or z[a:b][:,c:d]
    z = numpy.array([[0, 10, 20, 30, 40],[50, 60, 70, 80, 90]])

    print z[:1,:]  # Row 0, all columns
    # [[ 0 10 20 30 40]]

    print z[:1]  # Same as Row 0, all columns
    # [[ 0 10 20 30 40]]

    print z[:,:1]  # All Rows, column 0
    # [[ 0]
    # [50]]

    print z[:1,0:3]  # Row 0, columns 0 to 2
    # [[ 0 10 20]]

    print z[:1][:,0:3]  # Same as Row 0, columns 0 to 2
    # [[ 0 10 20]]

    print z[:,3:]  # All rows, columns 3 and 4
    # [[30 40]
    # [80 90]]

    print numpy.ndim(z[1:2,:])  # Returns dimensions  # 2


if __name__ == '__main__':
    #single_array_example()
    #multiple_arrays_example()
    #matrix_example()
    #array_selection()
    array_slicing()
