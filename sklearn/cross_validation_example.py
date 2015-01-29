'''
    Using K-fold cross validation; provides train/test indices to split data
    into train test sets.  Split dataset into k consecutive folds (no shuffle)
'''


import numpy as np
from sklearn import cross_validation


if __name__ == '__main__':

    X = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    y = np.array([1, 2, 3, 4])

    kf = cross_validation.KFold(n=4, n_folds=2, random_state=1234, shuffle=False)
    print len(kf)  # 2
    print(kf)

    for train_index, test_index in kf:
        print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        #('TRAIN:', array([2, 3]), 'TEST:', array([0, 1]))
        #('TRAIN:', array([0, 1]), 'TEST:', array([2, 3]))
