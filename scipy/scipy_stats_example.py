""" SciPy Stats is a module that contains a large number of probability
   distributions as well as statistical functions.  Each distribution is
   an instance of the class 'rv_continuous'.
   Reference at http://docs.scipy.org/doc/scipy/reference/stats.html

   """


import numpy as np
import scipy as sp
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt


def descriptive_statistics():

    my_data = sp.randn(100)  # 100 random numbers
    print len(my_data)  # 100

    #print my_data
    # [ -9.90322017e-01   1.15233159e-01  -2.93076899e-02  -2.17625707e-01
    #   -1.27680249e-02   5.14887346e-01   1.89355659e-01   1.52055706e+00...]

    ### NumPy - some basic functions from numpy and scipy overlap

    print ("Mean: {0:8.6f}".format(np.mean(my_data)))
    # Mean: 0.094097

    print ("Minimum: {0:8.6f}".format(np.min(my_data)))
    # Minimum: -2.437701

    print ("Maximum: {0:8.6f}".format(np.max(my_data)))
    # Maximum: 2.333469

    print ("Median: {0:8.6f}".format(np.median(my_data)))
    # Median: 0.084608

    ### SciPy

    print ("Variance with N in denominator: {0:8.6f}".format(sp.var(my_data)))
    # Variance with N in denominator: 1.011191

    print ("Variance with N-1 in denominator: {0:8.6f}".format(sp.var(my_data, ddof=1)))
    # Variance with N-1 in denominator: 1.021405

    print ("Std. Deviation: {0:8.6f}".format(sp.std(my_data)))
    # Std. Deviation: 1.005580

    print ("Skew: {0:8.6f}".format(stats.skew(my_data)))
    # Skew: -0.085338

    print ("Kurtosis: {0:8.6f}".format(stats.kurtosis(my_data)))
    # Kurtosis: -0.511248

    print ("Describe: "), stats.describe(my_data)
    # Size, min_max, mean, unbiased variance, biased skewness, biased kurtosis
    # Describe:  (100, (-2.4377012896025145, 2.3334691771084399),
    # 0.094097496646427678, 1.0214049630113344, -0.08533767838609484,
    # -0.5112479832958332)


def continuous_probability_distribution():
    """ Examples include:
        * norm: Normal or Gaussian
        * chi2: Chi-squared
        * t: Student's T
        * uniform: Uniform
    """
    print "Continuous Probability Distributions"
    # TODO: http://oneau.wordpress.com/2011/02/28/simple-statistics-with-scipy/


def discrete_probability_distribution():
    """ Examples include:
        * binom: Binomial
        * poisson: Poisson
    """
    print "Discrete Probability Distributions"


def statistical_functions():
    """ Examples include:
        * mode: Modal value
        * moment: central moment
        * describe: descriptive statistics
        * histogram: histogram of data
    """
    print "Statistical functions"

if __name__ == '__main__':

    descriptive_statistics()
    continuous_probability_distribution()
