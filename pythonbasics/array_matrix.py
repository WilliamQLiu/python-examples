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


if __name__ == '__main__':
    single_array_example()
    multiple_arrays_example()
    matrix_example()
