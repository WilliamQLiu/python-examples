""" Working through examples from Wes McKinney's Python for Data Analysis
    Examples include:
      1.) reshaping data with hierarchical indexing
      
"""

import pandas
import numpy

def stack_basic():
    data = pandas.DataFrame(numpy.arange(6).reshape(2, 3),
        index=pandas.Index(['Ohio', 'Colorado'],
        name='state'),
        columns=pandas.Index(['one', 'two', 'three'], name='number'))
    print "Basic DataFrame: \n", data, "\n"


if __name__ == '__main__':
    stack_basic()