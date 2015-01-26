'''
    pipeline can be used to chain multiple estimators into one.  This is
    useful as there is often a fixed sequence of steps in processing the
    data, for example feature selection, normalization and classification

    Convenience - only have to fit and predict once on your data
    All estimators in a pipeline (except last one) must have a transform method
    The last estimator may be any type (transformer, classifier, etc)
    Allows 'grid search' over parameters of all estimators in pipeline at once
'''

import numpy as np
import pylab as pl
from sklearn import datasets, feature_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV


if __name__ == '__main__':

    # Load data
    news = datasets.fetch_20newsgroups()
    X, y = news.data, news.target

    # Feature extraction: vectorizer
    # For some types of data a feature extraction must be applied to
    # convert to numerical features using fit and transform
    vectorizer = TfidfVectorizer()  # features are each word
    vectorizer.fit(X)  # fit applies to training set
    vector_X = vectorizer.transform(X)  # transform can be used on train or test
    print vector_X.shape  # (11314, 130107)

    # Feature selection
    # Select features that seem relevant for a learning task
    # Selection strategies include: FDR, FPR, FWER, k-best, percentile
    # choice of parameter 'score_func' is important, use the following:
    #  * f_regression for regression problems
    #  * f_clasif for classification problems
    #  * chi2 for classification problems with sparse non-negative data (e.g. text)
    selector = feature_selection.SelectPercentile(percentile=5,
            score_func=feature_selection.chi2)
    X_red = selector.fit_transform(vector_X, y)
    print "Original data shape %s, reduced data shape %s" % (vector_X.shape, X_red.shape)

    # Pipelining takes a list of (name, estimator) pairs that are applied on
    # the data in the order of the list.  Pipeline object exposes fit,
    # transform, predict and score methods that result from applying the
    # transforms (and fit in the case of the fit method) one after the other
    # to the data, and calling the last object's corresponding function
    # We can combine our feature extraction, selection and final SVC in one step
    svc = LinearSVC()
    pipeline = Pipeline([('vectorize', vectorizer), ('select', selector), ('svc', svc)])
    cross_val_score(pipeline, X, y, verbose=3)
    # [CV] no parameters to be set .........................................
    # [CV] ................ no parameters to be set, score=0.888212 -   4.2s
    # [Parallel(n_jobs=1)]: Done   1 jobs       | elapsed:    4.2s
    # [CV] no parameters to be set .........................................
    # [CV] ................ no parameters to be set, score=0.891068 -   4.2s
    # [CV] no parameters to be set .........................................
    # [CV] ................ no parameters to be set, score=0.888741 -   4.4s
    # [Parallel(n_jobs=1)]: Done   3 out of   3 | elapsed:   12.8s finished

    # Parameter selection - pipeline returned a lot of different parameters
    # Pipeline object exposes the parameters of the estimators it wraps with
    # the following convention: name of the estimator, __, name of parameter
    pipeline.set_params(svc__C=10)  # set SVC's C parameter

    # Choosing parameters by cross-validation may imply running transformers
    # many times on the same data with the same parameters.  Can avoid overhead
    # by using joblib's memory
    memory = joblib.Memory(cachedir='.')
    memory.clear()
    selector.score_func = memory.cache(selector.score_func)

    # GridSearchCV - Use gridsearch to choose the best C between 3 values
    grid = GridSearchCV(estimator=pipeline, param_grid=dict(svc__C=[1e-2, 1, 1e2]))
    grid.fit(X, y)
    print grid.best_estimator_.named_steps['svc']