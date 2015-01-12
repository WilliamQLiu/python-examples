""" joblib can help with:
    * Memory class defines a context for lazy evaluation of a function by
      storing the results to the desk and not rerunning the function twice for
      the same arguments (good for large input and output data like np arrays)

    * joblib provides a simple helper class to write parallel for loops using
      Python's 'multiprocessing' module (default).  Write the code to be
      executed as a generator expression, and convert it to parallel computing

    * joblib can dump (fast persistence of an object into a file, with
      dedicated storage for numpy arrays) and load (reconstruct an object from
      a file persisted with joblib.dump)
"""


import numpy as np
from math import sqrt
#from tempfile import mkdtemp  # for making temp directory
from joblib import Memory, Parallel, delayed, dump, load
from timeit import Timer  # for timing functions
import shutil  # clean up temporary folders after done with computation
from sklearn import datasets  # for load and dump example
from sklearn import svm  # Classifier: Support Vector Machine

#cache_dir = mkdtemp('/tmp/joblib/')  # Make temp directory for caching
mem = Memory(cachedir='/tmp/joblib/', verbose=0)  # specify temp dir for cache


@mem.cache  # decorate function to be cached
def my_function(x):
    """ Custom function """
    print "Running f(%s)" % x
    return x


def memory_example():
    """ Create a Vandermonde matrix, when we call function (square) twice with
    the same argument, it does not get executed the second time, and the output
    gets loaded from the pickle file.  Can also use with custom functions """
    a = np.vander(np.arange(3)).astype(np.float)  # create a Vandermonde matrix
    square = mem.cache(np.square)  # remembers operation
    b = square(a)
    c = square(a)  # Does not need to reexecute since second time, same arg
    d = square(b)  # Does need to reexecute since different arg

    print my_function(10)  # runs for the first time
    print my_function(10)  # does not need to reexecute since same arg
    print my_function(20)  # needs to reexecute since different arg
    print my_function(10)  # does not need to reexecute since same arg


def parallel_example(my_jobs):
    """ Running jobs in parallel by specifying n_jobs for X CPUs.  The
    'delayed' function is a trick to be able to create a tuple with a
    function-call syntax"""
    Parallel(n_jobs=my_jobs, verbose=50)(delayed(sqrt)(i**2) for i in range(10000))
    print "Done executing parallel job with ", my_jobs, " jobs"


if __name__ == '__main__':
    ### Run examples of memory and parallel
    memory_example()  # Good for complex i/o objects (like large numpy arrays)
    #parallel_example(1)  # Run a job with a single core
    #parallel_example(4)  # Run a job in parallel

    ### Time difference in processing time
    t = Timer(lambda: parallel_example(3))  # 2 seconds
    print "  Execution Time is: ", t.timeit(number=1)
    print "\n"

    t = Timer(lambda: parallel_example(1))  # 3.2 seconds
    print "  Execution Time is: ", t.timeit(number=1)
    print "\n"

    ### Load and Dump data
    clf = svm.SVC()  # Specify classifier
    iris = datasets.load_iris()  # Load data
    X, y = iris.data, iris.target  # Split to X, Y
    clf.fit(X, y)  # Fit to model

    print "Classifier is: ", clf

    print "Saving Data"
    save_me = dump(clf, 'save_me.pk1')  # Dump data
    print save_me

    print "Loading Data"
    clf = load('save_me.pk1')  # Load data
    print clf

    ### Remove temp directories
    try:
        shutil.rmtree('/tmp/joblib/')
        print "Removed temporary folder"
    except OSError:
        pass  # Can sometimes fail in Windows
