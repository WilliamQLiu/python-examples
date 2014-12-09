""" Using Scikits-learn to create linear models and regularization operations
  * models relationship between y and X
  * scalar dependent variable y and one or more explanatory variables denoted X
  * if just one explanatory variable (X), is 'simple linear regression'
  * if more than one explanatory variable (X), is 'multiple linear regression'
 """

from sklearn import linear_model

def ordinary_least_squares_example():
    """ Fits a linear classifier/model with coefficients to minimize the 
    residual sum of squares between the observed responses and the predicted
    responses by the linear approximation """
    print "Ordinary Least Squares"
    classifier = linear_model.LinearRegression()
    X = [[0,0], [1,1], [2,2]]
    y = [0, 1, 2]
    classifier.fit(X, y)
    print "  Classifier coefficient is: ", classifier.coef_
    print "  Classifier intercept is: ", classifier.intercept_
    print "  Classifier score is:", classifier.score(X, y)

    # Disadvantages
    # Coefficient estimates for Ordinary Least Squares rely on the
    # indepednence of the model terms.  When terms are correlated and the
    # columns of the design matrix have an approximate linear dependence,
    # the design matrix becomes close to singular and as a result,
    # the least-squares estimate becomes highly sensitive to random errors
    # in the observed response, producing a large variance - see error below
    
    # Multicollinerarity - is a linear association between two explanatory
    # variables 

def ridge_regression_example():
    """Ridge Regression, also known as Tikhonov-Miller method
    Addresses some of the problems of Ordinary Least Squares by imposing a
    penalty on the size of coefficients.  The ridge coefficients minimize a
    penalized residual sum of squares
    """

    print "Ridge Regression Example"
    classifier = linear_model.Ridge(alpha = .5)
    X = [[0, 0], [0, 0], [1, 1]]
    y = [0, .1, 1]
    classifier.fit(X, y)
    print "  Classifier coefficient is: ", classifier.coef_
    print "  Classifier intercept is: ", classifier.intercept_
    print "  Classifier score is:", classifier.score(X, y)

    # Ridge Regression's coefficient is more robust to collinerarity
    # Same order of complexity as Ordinary Least Squares

def ridge_regression_crossvalidate_example():
    """ Ridge Regression with built-in cross validation of the alpha parameter
    """

    print "Ridge Regression with built-in Cross Validation Example"
    classifier = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
    X = [[0, 0], [0, 0], [1, 1]]
    y = [0, .1, 1]
    classifier.fit(X, y)
    print "  Classifier coefficient is: ", classifier.coef_
    print "  Classifier intercept is: ", classifier.intercept_
    print "  Classifier score is:", classifier.score(X, y)

def lasso_example():
    """ Lasso is a regularization technique for linear models that estimates
     sparse coefficients.  It is used due to its tendency to prefer solutions 
    with fewer parameter values.  Use lasso to reduce the number of predictors
    in a generalized linear model, identify important predictors, select among
    redundant predictors, and produce shrinkage estimates with potentially
    lower predictive errors than ordinary least squares.  Examples include the
    field of compressive sensing"""

    print "Lasso Regularization Technique"
    classifier = linear_model.Lasso(alpha=0.1)
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    classifier.fit(X, y)
    print "  Classifier coefficient is: ", classifier.coef_
    print "  Classifier intercept is: ", classifier.intercept_
    print "  Classifier score is:", classifier.score(X, y)
    print "  Classifier predict for [[1, 1]] is: ", classifier.predict([[1, 1]])

    # Lasso can be used for feature prediction, which can reduce the
    # dimensionality of the data to use with another classifier
    # The higher the alpha parameter, the fewer features selected

if __name__ == "__main__":
    
    ordinary_least_squares_example()
    ridge_regression_example()
    ridge_regression_crossvalidate_example()

    ### Regularization refers to the method of preventing overfitting by
    # explicitly controlling model complexity.  We have two techniques
    # to ensure low variance, low bias
    # L1, Lasso regularization and L2, Ridge regularization
    lasso_example() # L1, LaPlace Prior: Biased, low Variance
    # L2, Gaussian Prior: Unbiased, high Variance
    
    ### Evaluation Metrics
    # Statistical accuracy metrics evaluate the accuracy of a system by
    # comparing the numerical recommendation scores against the actual user
    # ratings for the user-item pairs in the test dataset
    # Mean Absolute Error (MAE) between ratings and predictions is a 
    # widely used metric; the lower the MAE the more accurate the recommendation
    # engine predicts user ratings