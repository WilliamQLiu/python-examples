""" sklearn > naive_bayes > MultinomialNB
    Naive Bayes classifier for multinominal models

    The multinomial Naive Bayes classifier is for classification with discrete
    features (e.g. word counts for text classification).  The multinominal
    distribution normally requires integer feature counts.  However, fractional
    counts such as tf-idf may also work.

    Parameters
      alpha : float, optional (default=1.0)
        Additive (Laplace/Lidstone) smoothing parameter
      fit_prior : boolean.  Whether to learn class prior probabilities or not
      class_prior : array-like, size (n_classes,) - prior probabilities of the
        classes.  
"""

import numpy as np
from sklearn.naive_bayes import MultinomialNB

X = np.random.randint(5, size=(6, 20))
print "X is \n", X
y = np.array([1, 2, 3, 4, 5, 6])
print "y is \n", y

clf = MultinomialNB() # classifier for Naive Bayes multinomial models
clf.fit(X, y)
print clf.fit(X, y) # Fit the Naive Bayes classifier according to X, y
print(clf.predict(X[2])) # Predict Probability estimates for test vector X
print "Score is ", clf.score(X, y) # Mean accuracy on the given test data

# print clf.feature_count_ # See # of samples for each (class, feature) during
# fitting X
#print clf.class_count_ # See the # of samples for each class during fitting y
