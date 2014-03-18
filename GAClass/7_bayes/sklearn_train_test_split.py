""" sklearn > cross_validation > train_test_split
    Split arrays or matrices into random train and test subsets

    Wraps calls to 'check_arrays' and next(iter(ShuffleSplit(n_samples)))
    and application to input data into a single call for splitting (and 
        optionally subsampling data in a oneliner)

    Parameters
      *arrays : sequence of arrays or scipy.sparse matrices with same shape[0]
      test_size : float, int, or None. Represent the proportion (float) or 
      absolute number (int) of test samples from the dataset
        If None, then test size is set to .25
      train_size : float, int, or None. Represent the proportion (float) or
      absolute number (int) of test samples from the entire dataset.
        If None, then train_size is complement of the test size
      random_state : pseudo-random number generator state for random sampling
      dtype : a numpy dtype instance

 """
import numpy as np
from sklearn.cross_validation import train_test_split

a, b = np.arange(10).reshape((5, 2)), range(5)
# a is 5 rows, 2 columns, values from 0 - 9
# b is a list with values from 0 - 4

print "A is \n", a
print "B is \n", b

a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.33,
    random_state=42)

print "A Train \n", a_train # 3 rows, 2 columns, [[4 5][0 1][6 7]]
print "A Test \n", a_test # 2 rows, 2 columns [[2 3][8 9]]
print "B Train \n", b_train # list with values [2 0 3]
print "B Test \n", b_test # list with values [1 4]
