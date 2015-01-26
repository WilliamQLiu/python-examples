""" sklearn > pipeline > Pipeline
    Pipeline of transforms with a final estimator
    Sequentially apply a list of transforms and a final estimator
    Intermediate steps of the pipeline must be 'transforms' (implement fit
        and transform methods).  Final estimator needs only implement fit

    Purpose of the pipeline is to assemble several steps that can be cross-
    validated together while setting different parameters.  It enables setting
    parameters of the various steps using their names and the parameter name
    separated by a '__'

    Parameters : steps : list (list of name, transforms) that are chained

"""

from sklearn import svm
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline

# Generate some data to play with
X, y = samples_generator.make_classification(n_informative=5, n_redundant=0,
    random_state=42)

print "X is \n", X
print "y is \n", y

# ANOVA SVM-C
anova_filter = SelectKBest(f_regression, k=5)
clf = svm.SVC(kernel='linear')
anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])

# You can set the parameters using the names issued
# For instance, fit using a k of 10 in the SelectKBest
# and a parameter 'C' of the svn
anova_svm.set_params(anova__k=10, svc__C=.1).fit(X,y)

prediction = anova_svm.predict(X)
print "Prediction is \n", prediction
anova_svm.score(X, y)
print "Score is ", anova_svm.score(X, y)