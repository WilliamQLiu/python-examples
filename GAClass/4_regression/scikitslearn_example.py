""" Using Scikits-learn to offer regularization operations and more robust methods """
# models relationship between y and X
# scalar dependent variable y and one or more explanatory variables denoted X
# if just one explanatory variable (X), then is 'simple linear regression'
# if more than one explanatory variable (X), then is 'multiple linear regression'

from sklearn.linear_model import LinearRegression
from sklearn import linear_model

def linear_regression_example():
    model = LinearRegression() 
    model = model.fit(X,y)
    model.score(X,y)
    print model

def linear_model_example():
    model = linear_model.Ridge(alpha = .5)
    model.fit(X,y)
    print model.coef_

def linear_model_cv_example():
    model = linear_model.RidgeCV(alpha = [0.1, 1.0, 10.0])
    model.fit(X,y)
    print model.coef_
    print model.alpha_

if __name__ == "__main__":
    linear_regression_example()
    linear_model_example()
    linear_model_cv_example()